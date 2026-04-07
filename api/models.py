from django.contrib.postgres.fields import ArrayField
from django.db import models


class StackIcon(models.Model):
    class IconChoices(models.TextChoices):
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

    icon = models.CharField(max_length=100, choices=IconChoices.choices, unique=True)
    icon_text = models.CharField(
        max_length=100, blank=True, default="", verbose_name="Optional text to display next to the icon"
    )
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ("order",)

    def __str__(self):
        return self.icon_text or self.icon


class Experience(models.Model):
    type = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    tags = ArrayField(models.CharField(max_length=100), blank=True)

    class Meta:
        ordering = ("-date",)

    def __str__(self):
        return self.title
