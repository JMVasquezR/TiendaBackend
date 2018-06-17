from django.contrib.auth import get_user_model
from django.db import models, transaction
import os

user_model = get_user_model()

TIPO_PATRON = (
    (0, 'Numerico'),
    (1, 'Alfanumerico'),
)

TIPO_CONTRIBUYENTE = (
    (0, 'Documento para nacionales solamente'),
    (1, 'Documento para extranjeros solamente'),
    (2, 'Documento para nacionales y extranjeros'),
)

TIPO_LONGITUD = (
    (0, 'Exacta'),
    (1, 'Inexacta'),
)


class TipoDocumento(models.Model):
    nombre = models.CharField(blank=False, null=False, max_length=100, unique=True)
    tipo_patron = models.IntegerField(blank=False, null=False, choices=TIPO_PATRON)
    tipo_contribuyente = models.IntegerField(blank=False, null=False, choices=TIPO_CONTRIBUYENTE)
    tipo_longitud = models.IntegerField(blank=False, null=False, choices=TIPO_LONGITUD)
    longitud = models.IntegerField(blank=False, null=False, default=0)


class Persona(models.Model):
    def image_path(instance, filename):
        filename, file_extension = os.path.splitext(filename)
        return os.path.join('Persona', 'persona-' + instance.numero_documento + file_extension)

    class Meta:
        permissions = (
            # BEGIN permisos para Crud de paciente
            ("puede_crear_sus_pacientes", "Puede crear sus pacientes"),
            ("puede_crear_otros_pacientes", "Puede crear otros pacientes"),
            ("puede_listar_sus_pacientes", "Puede listar sus pacientes"),
            ("puede_listar_todos_los_pacientes", "Puede listar todos los pacientes"),
            ("puede_editar_sus_pacientes", "Puede editar sus pacientes"),
            ("puede_editar_todos_los_pacientes", "Puede editar todos los pacientes"),
            ("puede_deshabilitar_sus_pacientes", "Puede deshabilitar sus pacientes"),
            ("puede_deshabilitar_todos_los_pacientes", "Puede deshabilitar todos los pacientes"),
            ("puede_relacionar_doctor_a_paciente", "Puede (des)relacionar doctor a pacientes"),
            # END permisos para Crud de paciente
            ("puede_listar_todos_los_doctores", "Puede listar todos los doctores"),
            ("puede_crear_doctor", "Puede crear doctor"),
            ("puede_listar_evento_clinicos_de_paciente", "Puede listar eventos clinicos de pacientes"),
            ("puede_ver_detalle_evento_clinico", "Puede ver detalle de vento clinico"),
            ("puede_crear_cambio_de_metodo", "Puede crear cambio de metodo"),
        )

    user = models.ForeignKey(user_model, on_delete=models.CASCADE, blank=True, null=True)
    correo = models.EmailField(blank=False, null=False)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido_paterno = models.CharField(max_length=100, blank=False, null=False)
    apellido_materno = models.CharField(max_length=100, blank=False, null=True)
    numero_documento = models.CharField(max_length=25, blank=False, null=False)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField(blank=False, null=False)

    # metadata
    fecha_creacion = models.DateTimeField(auto_now=False, auto_now_add=True)
    fecha_activacion = models.DateTimeField(auto_now=False, auto_now_add=True)

    es_cliente = models.BooleanField(default=False)

    def create_user_account(self, **kwargs):
        django_user = user_model.objects.create(
            username=self.correo,
            email=self.correo,
            is_active=False,
            first_name=self.nombre,
            last_name=' '.join([x for x in [self.apellido_paterno, self.apellido_materno] if x])
        )
        django_user.set_unusable_password()
        django_user.save()
        self.user = django_user
        super(Persona, self).save()
        return django_user

    @transaction.atomic()
    def save(self, *args, **kwargs):
        if self.pk:
            super().save(*args, **kwargs)
        else:
            self.create_user_account()

    def full_name(self):
        full_name = '%s %s %s' % (self.nombre, self.apellido_paterno, self.apellido_materno)
        return full_name.strip()

    def delete(self, using=None, keep_parents=False):
        self.user.is_active = False
        self.user.save()


class Cliente(Persona):
    default_group = None

    class Meta:
        proxy = True

    class DoctorManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(es_cliente=True)

    objects = DoctorManager()

    def create_user_account(self, **kwargs):
        django_user = super().create_user_account(**kwargs)
        self.es_cliente = True
        super(Persona, self).save()
        return django_user
