from django.contrib.contenttypes.models import ContentType
from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label=u'last login',
            name='last_login',
            format='d.m.Y',
            allow_blank=False,
            anchor='100%')

        self.field__superuser_status = ext.ExtCheckBox(
            label=u'superuser status',
            name='is_superuser',
            allow_blank=False,
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            allow_blank=False,
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label=u'last name',
            name='last_name',
            allow_blank=False,
            anchor='100%')

        self.field__email_address = ext.ExtStringField(
            label=u'email address',
            name='email',
            allow_blank=False,
            anchor='100%')

        self.field__staff_status = ext.ExtCheckBox(
            label=u'staff status',
            name='is_staff',
            allow_blank=False,
            anchor='100%')

        self.field__active = ext.ExtCheckBox(
            label=u'active',
            name='is_active',
            allow_blank=False,
            anchor='100%')

        self.field__date_joined = ext.ExtDateField(
            label=u'date joined',
            format='d.m.Y',
            name='date_joined',
            anchor='100%')

    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__superuser_status,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email_address,
            self.field__staff_status,
            self.field__active,
            self.field__date_joined
        ))

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class PermissionAddWindow(BaseEditWindow):
    def _init_components(self):
        super(PermissionAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%'
        )

        content_types = ContentType.objects.all()
        content_type_choices = [(c.id, c.name) for c in content_types]
        self.field__content_types = make_combo_box(
            label=u'content type',
            name='content_type_id',
            allow_blank=False,
            anchor='100%',
            data=content_type_choices)

        self.field__codename = ext.ExtStringField(
            label=u'codename',
            name='codename',
            allow_blank=False,
            anchor='100%'
        )

    def _do_layout(self):
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_types,
            self.field__codename
        ))

    def set_params(self, params):
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'