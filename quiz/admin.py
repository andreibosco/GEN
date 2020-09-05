from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.forms import ModelForm
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field
from modeltranslation.admin import (
    TabbedTranslationAdmin,
    TranslationStackedInline,
    TranslationTabularInline,
)

# from django.contrib.admin.widgets import FilteredSelectMultiple

from .forms import QuizAdminForm
from .models import (
    Likert,
    LikertAnswer,
    LikertAttempt,
    MCAnswer,
    MCQuestion,
    MCQuestionAttempt,
    OpenEnded,
    OpenEndedAttempt,
    Question,
    QuestionAttempt,
    QuestionGroupHeader,
    Quiz,
    QuizScore,
)


def duplicate(modeladmin, request, queryset):
    for item in queryset:
        item.duplicate()


duplicate.short_description = "Duplicate selected items"

# Classes AlwaysChangedModelForm and CheckerInline were based on:
# https://stackoverflow.com/questions/34355406/django-admin-not-saving-\
# pre-populated-inline-fields-which-are-left-in-their-init


class AlwaysChangedModelForm(ModelForm):
    """
    Should returns True if data differs from initial.
    By always returning true even unchanged inlines will get validated and saved.
    """

    def has_changed(self):
        return True


class CheckerInline(TranslationStackedInline):
    """
    Base class for checker inlines
    """

    extra = 1  # defines the initial number of fields
    form = AlwaysChangedModelForm


class QuestionInline(SortableInlineAdminMixin, TranslationTabularInline):
    """
    Class for creating a sortable inline tabular layout for questions.
    """

    # Tip: admin.TabularInline can be switched with admin.StackedInline
    # Documentation at
    # https://django-admin-sortable2.readthedocs.io/en/latest/usage.html\
    # make-a-stacked-or-tabular-inline-view-sortable
    model = Question
    # include = ['quiz', 'content']
    exclude = [
        "explanation",
    ]
    extra = 0


class QuizAdmin(TabbedTranslationAdmin):
    # list_display = ("name", "course", "quiz_actions")
    list_display = ("name", "course", "section", "video")
    list_filter = ("course", "section")
    # search_fields = ('description', 'course', )
    inlines = (QuestionInline,)
    actions = [duplicate]
    form = QuizAdminForm
    save_as = True

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "description",
                    "author",
                    "start_date",
                    "end_date",
                    "course",
                    "section",
                    "published",
                    "video",
                    "requirement",
                )
            },
        ),
        (
            "Answer submission options",
            {
                "fields": (
                    "require_answers",
                    "allow_multiple_attempts",
                    "attempts_max_number",
                )
            },
        ),
        (
            "Scoring options",
            {"fields": ("check_score", "show_score", "show_correct_answers")},
        ),
        (
            "Assessment options",
            {
                "fields": (
                    "assessment_method",
                    "assessment_min_percentage",
                    "assessment_max_mistakes",
                )
            },
        ),
    )

    # filter_horizontal = ('questions', )

    # def get_urls(self):
    #     urls = super().get_urls()
    #     custom_urls = [path("copy/", self.duplicate_quiz)]
    #     return custom_urls + urls

    # def quiz_actions(self, obj):
    #     return format_html('<a class="button" href="#">Make a copy</a>',)


class QuizScoreResource(resources.ModelResource):
    quiz = Field(attribute="quiz__name", column_name="quiz_name")
    course = Field(attribute="course__name", column_name="course_name")
    course_code = Field(attribute="course__code", column_name="course_code")
    section = Field(attribute="quiz__video__section__name", column_name="section_name")
    video = Field(attribute="quiz__video__name", column_name="video_name")
    video_internal_name = Field(
        attribute="quiz__video__internal_name", column_name="video_internal_name"
    )

    class Meta:
        model = QuizScore
        fields = (
            "id",
            "created",
            "student",
            "quiz",
            "video",
            "video_internal_name",
            "course",
            "course_code",
            "section",
            "score",
        )
        export_order = (
            "id",
            "created",
            "student",
            "course",
            "course_code",
            "section",
            "quiz",
            "video",
            "video_internal_name",
            "score",
        )


class QuizScoreAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ("student", "quiz", "course", "score")
    list_filter = ("quiz", "course", "student")

    resource_class = QuizScoreResource

    # search_fields = ('student', 'quiz', 'course')
    # filter_horizontal = ('student',)


class MCAnswerInline(SortableInlineAdminMixin, TranslationTabularInline):
    """
    Class to show multiple choice answers inline (tabular)
    """

    model = MCAnswer
    extra = 0


class LikertAnswerInline(CheckerInline):
    """
    Class to show likert answers inline (stacked), and based on
    CheckerInline to always save while submitting/creating a Likert
    object (even if the LikertAnswer fields are using the default values)
    """

    model = LikertAnswer


class QuestionAdmin(TabbedTranslationAdmin):
    """
    Base class for questions admin layout (editing).
    """

    list_display = ("content", "quiz", "created")
    list_filter = ("quiz",)
    search_fields = ("content", "explanation")
    # filter_horizontal = ('quiz',)

    class Media:
        css = {"all": ("css/admin.css",)}


class MCQuestionAdmin(QuestionAdmin):
    """
    Class for multiple choice question editing
    """

    # list_display = ('quiz',
    #                 'content', 'created')
    # list_filter = ('quiz', 'content')
    fields = (
        "question_type",
        "content",
        "quiz",
        "explanation",
        "multiple_correct_answers",
    )
    inlines = [MCAnswerInline]

    class Media:
        css = {"all": ("css/admin.css",)}

    # setting question_type value to Multiple Choice
    def get_form(self, request, obj=None, **kwargs):
        form = super(MCQuestionAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["question_type"].initial = "M"
        return form


class MCAnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "content", "check")
    list_filter = ("question",)

    class Media:
        css = {"all": ("css/admin.css",)}


class LikertAdmin(QuestionAdmin):
    """
    Class for likert question editing
    """

    fields = ("question_type", "content", "quiz")
    inlines = [LikertAnswerInline]
    # readonly_fields = ["question_type"]

    class Media:
        css = {"all": ("css/admin.css",)}

    # setting question_type value to Likert
    def get_form(self, request, obj=None, **kwargs):
        form = super(LikertAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["question_type"].initial = "L"
        return form


class LikertAnswerAdmin(TabbedTranslationAdmin):
    list_display = ("question", "scale_range", "check_answer", "answer_range")
    list_filter = ("question__quiz__course", "question__quiz", "question__quiz__video")

    class Media:
        css = {"all": ("css/admin.css",)}


class OpenEndedAdmin(QuestionAdmin):
    fields = ("question_type", "content", "quiz")

    class Media:
        css = {"all": ("css/admin.css",)}

    # setting question_type value to Open Ended
    def get_form(self, request, obj=None, **kwargs):
        form = super(OpenEndedAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["question_type"].initial = "O"
        return form


class QuestionAttemptResource(resources.ModelResource):
    quiz_name = Field(attribute="quiz__name", column_name="quiz_name")
    course_name = Field(attribute="course__name", column_name="course_name")
    course_code = Field(attribute="course__code", column_name="course_code")
    section_name = Field(attribute="section__name", column_name="section_name")
    question_type = Field(
        attribute="question__question_type", column_name="question_type"
    )
    question_content = Field(
        attribute="question__content", column_name="question_content"
    )
    video_name = Field(attribute="video__name", column_name="video_name")
    video_internal_name = Field(
        attribute="video__internal_name", column_name="video_internal_name"
    )

    class Meta:
        model = QuestionAttempt
        fields = (
            "id",
            "created",
            "student",
            "quiz_name",
            "course_name",
            "course_code",
            "section_name",
            # "attempt_number",
            "question_type",
            "question_content",
            "multiplechoice_answer__content",
            "video_name",
            "video_internal_name",
            "answer_content",
            "correct",
        )
        export_order = (
            "id",
            "created",
            "student",
            "course_name",
            "course_code",
            "section_name",
            "quiz_name",
            # "attempt_number",
            "video_name",
            "video_internal_name",
            "question_type",
            "question_content",
            "multiplechoice_answer__content",
            "answer_content",
            "correct",
        )


class QuestionAttemptAdmin(ExportActionMixin, admin.ModelAdmin):
    """
    Base class for quiz questions (likert, multiple choice, and open ended).
    All questions models follow the same naming pattern.
    """

    list_display = (
        "question",
        "student",
        "course",
        "quiz",
        # "question",
        "attempt_number",
        "created",
    )
    # list_filter = ("course", "quiz", "question", "attempt_number")
    list_filter = ("course", "student", "quiz", "attempt_number")
    resource_class = QuestionAttemptResource

    # search_fields = ('quiz', 'course', 'question', 'student')


class QuestionGroupHeaderAdmin(QuestionAdmin):
    # list_display = ('content',)
    # filter_horizontal = ('quiz',)
    fields = ("question_type", "content", "quiz")

    # setting question_type value to Group Header
    def get_form(self, request, obj=None, **kwargs):
        form = super(QuestionGroupHeaderAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields["question_type"].initial = "H"
        return form


# TODO: comment Question, MCAnswer, LikertAnswer (they can be edited using the
# question page and are only useful during testing and development)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(MCQuestion, MCQuestionAdmin)
admin.site.register(MCQuestionAttempt, QuestionAttemptAdmin)
admin.site.register(MCAnswer, MCAnswerAdmin)
admin.site.register(QuizScore, QuizScoreAdmin)
admin.site.register(Likert, LikertAdmin)
admin.site.register(LikertAnswer, LikertAnswerAdmin)
admin.site.register(LikertAttempt, QuestionAttemptAdmin)
admin.site.register(OpenEnded, OpenEndedAdmin)
admin.site.register(OpenEndedAttempt, QuestionAttemptAdmin)
admin.site.register(QuestionGroupHeader, QuestionGroupHeaderAdmin)
admin.site.register(QuestionAttempt, QuestionAttemptAdmin)
