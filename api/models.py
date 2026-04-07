from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db import models


class TechnologyChoices(models.TextChoices):
    PYTHON = "python", "Python"
    DJANGO = "django", "Django"
    DOCKER = "docker", "Docker"
    KUBERNETES = "kubernetes", "Kubernetes"
    GITLAB = "gitlab", "GitLab"
    GITHUB = "github", "GitHub"
    GIT = "git", "Git"
    TYPESCRIPT = "typescript", "TypeScript"
    JAVASCRIPT = "javascript", "JavaScript"
    NEXTJS = "nextjs", "Next.js"
    REACT = "react", "React"
    NODEJS = "nodejs", "Node.js"
    POSTGRESQL = "postgresql", "PostgreSQL"
    POSTGRES = "postgres", "PostgreSQL"
    REDIS = "redis", "Redis"
    TAILWIND = "tailwind", "Tailwind CSS"
    HTML = "html", "HTML"
    CSS = "css", "CSS"
    AWS = "aws", "AWS"
    NGINX = "nginx", "Nginx"
    LINUX = "linux", "Linux"
    BASH = "bash", "Bash"
    GRAPHQL = "graphql", "GraphQL"
    REST = "rest", "REST API"
    MONGODB = "mongodb", "MongoDB"
    MYSQL = "mysql", "MySQL"
    C = "c", "C"
    CPLUSPLUS = "c++", "C++"
    CSHARP = "c#", "C#"
    MATHEMATICA = "mathematica", "Mathematica"
    MATLAB = "matlab", "MATLAB"


class StackIcon(models.Model):
    icon = models.CharField(max_length=100, choices=TechnologyChoices.choices, unique=True)
    icon_text = models.CharField(
        max_length=20, blank=True, default="", verbose_name="Optional text to display next to the icon"
    )
    order = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.icon_text or self.icon


class Experience(models.Model):
    class CategoryChoices(models.TextChoices):
        WORK = "work", "Berufliche Erfahrung"
        EDUCATION = "education", "Ausbildung"

    category = models.CharField(max_length=20, choices=CategoryChoices.choices)
    start_date = models.DateField(verbose_name="Startdatum")
    end_date = models.DateField(
        blank=True, null=True, verbose_name="Enddatum", help_text="Leer lassen für laufende Positionen"
    )
    organization = models.CharField(max_length=200, verbose_name="Firma/Institution")
    position = models.CharField(max_length=200, verbose_name="Position/Rolle")
    stack = ArrayField(
        models.CharField(max_length=100, choices=TechnologyChoices.choices),
        blank=True,
        default=list,
        verbose_name="Verwendete Technologien",
    )

    class Meta:
        ordering = ("-start_date",)

    def __str__(self):
        return f"{self.position} @ {self.organization}"

    def clean(self):
        """Validate that only one experience can have an empty end_date (current position)"""
        super().clean()
        if self.end_date:
            # If end_date is set, ensure it's not before start_date
            if self.end_date < self.start_date:
                raise ValidationError({"end_date": "Das Enddatum darf nicht vor dem Startdatum liegen."})

    def save(self, *args, **kwargs):
        """Override save to call full_clean for validation"""
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def is_current(self):
        """Returns True if this is an ongoing experience (no end date)"""
        return self.end_date is None

    @property
    def date_range(self):
        """Returns formatted date range string"""
        start = self.start_date.strftime("%m/%Y")
        end = self.end_date.strftime("%m/%Y") if self.end_date else "Heute"
        return f"{start} - {end}"
