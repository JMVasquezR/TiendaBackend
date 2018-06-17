# Generated by Django 2.0.6 on 2018-06-16 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenDeCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('estado_compra', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100, null=True)),
                ('numero_documento', models.CharField(max_length=25)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_activacion', models.DateTimeField(auto_now_add=True)),
                ('es_cliente', models.BooleanField(default=False)),
            ],
            options={
                'permissions': (('puede_crear_sus_pacientes', 'Puede crear sus pacientes'), ('puede_crear_otros_pacientes', 'Puede crear otros pacientes'), ('puede_listar_sus_pacientes', 'Puede listar sus pacientes'), ('puede_listar_todos_los_pacientes', 'Puede listar todos los pacientes'), ('puede_editar_sus_pacientes', 'Puede editar sus pacientes'), ('puede_editar_todos_los_pacientes', 'Puede editar todos los pacientes'), ('puede_deshabilitar_sus_pacientes', 'Puede deshabilitar sus pacientes'), ('puede_deshabilitar_todos_los_pacientes', 'Puede deshabilitar todos los pacientes'), ('puede_relacionar_doctor_a_paciente', 'Puede (des)relacionar doctor a pacientes'), ('puede_listar_todos_los_doctores', 'Puede listar todos los doctores'), ('puede_crear_doctor', 'Puede crear doctor'), ('puede_listar_evento_clinicos_de_paciente', 'Puede listar eventos clinicos de pacientes'), ('puede_ver_detalle_evento_clinico', 'Puede ver detalle de vento clinico'), ('puede_crear_cambio_de_metodo', 'Puede crear cambio de metodo')),
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio_unitario', models.FloatField()),
                ('descuento', models.FloatField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_tienda.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('tipo_patron', models.IntegerField(choices=[(0, 'Numerico'), (1, 'Alfanumerico')])),
                ('tipo_contribuyente', models.IntegerField(choices=[(0, 'Documento para nacionales solamente'), (1, 'Documento para extranjeros solamente'), (2, 'Documento para nacionales y extranjeros')])),
                ('tipo_longitud', models.IntegerField(choices=[(0, 'Exacta'), (1, 'Inexacta')])),
                ('longitud', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='tipo_documento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_tienda.TipoDocumento'),
        ),
        migrations.AddField(
            model_name='persona',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ordendecompra',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_tienda.Persona'),
        ),
        migrations.AddField(
            model_name='ordendecompra',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_tienda.Producto'),
        ),
        migrations.AddField(
            model_name='factura',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_tienda.Persona'),
        ),
        migrations.AddField(
            model_name='factura',
            name='orden_de_compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_tienda.OrdenDeCompra'),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('app_tienda.persona',),
        ),
        migrations.AlterUniqueTogether(
            name='ordendecompra',
            unique_together={('cliente', 'producto')},
        ),
    ]
