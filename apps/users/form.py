# -*- coding: utf-8 -*-

from django import forms


class RegForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        label='用户名',
        error_messages={
            'max_length': '用户名最长16位',
            'required': '用户名不能为空',
        },
        widget=forms.widgets.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    password = forms.CharField(
        min_length=6,
        label='密码',
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    re_password = forms.CharField(
        min_length=6,
        label='确认密码',
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
