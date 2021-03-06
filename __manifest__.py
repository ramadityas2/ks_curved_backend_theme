# -*- coding: utf-8 -*-
{
    'name': "Weevy Arc Backend Theme",
    'summary': """
        Weevy Arc Backend Theme.
    """,
    'description': """
        Using the Arch Backend Theme, this module applies the Weevy default branding configuration:
        1. login page + remove 'Powered by Odoo' and 'Superuser' login button
        2. backend (admin) panel
        3. frontend (customer portal) view
        4. favicon
        5. webtitle
    """,
    'author': "Ksolves India Ltd.",
    'website': "https://www.ksolves.com",
    'license': 'OPL-1',
    'version': '15.0.1.0.7',
    'category': 'Themes/Backend',
    'depends': ['web', 'base_setup', 'mail', 'auth_signup','portal'],

    # always loaded
    'data': [
        'data/data.xml',
        'data/ks_drawer_colors.xml',
        'data/ks_color_theme.xml',
        'security/ir.model.access.csv',
        'security/curved_theme_security.xml',
        'views/views.xml',
        'views/ks_main_panel.xml',
        'views/templates.xml',
        'views/ks_assets_popup_animation.xml',
        'views/ks_login_page.xml',
        'views/ks_res_users_preferences.xml',
        'views/ks_res_config_settings_view.xml',
        'data/weevy_pwa_configuration.xml',
        'data/weevy_default_favicon.xml',
        'data/weevy_default_company_logo.xml',
        'views/weevy_favicon_extend.xml',
        'views/weevy_login_page_extend.xml',
        'views/weevy_portal_template_extend.xml',
    ],
    'images': [
        'static/description/Banner.jpg',
        'static/description/list_screenshot.gif',
    ],
    'assets': {
        'web.assets_qweb': [
            '/ks_curved_backend_theme/static/src/xml/ks_menu.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_left_sidebar_panel.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_switch_language.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_quick_settings.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_global_settings.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_fullscreen.xml',
            # '/ks_curved_backend_theme/static/src/xml/ks_search_panel.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_company_settings.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_bookmark.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_appdrawer_edit.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_calendar_view.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_image_template.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_login_background_color.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_login_background_image.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_menubar_darkmode_toggle.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_leftpanelmenu.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_userMenu.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_navbar.xml',
            '/ks_curved_backend_theme/static/src/xml/ks_action_menus.xml',
            '/ks_curved_backend_theme/static/src/js/widgets/ksListDocumentViewer.xml',
            # '/ks_curved_backend_theme/static/src/xml/Ks_throbber_inherit.xml',
        ],
        'web._assets_primary_variables': [
            '/ks_curved_backend_theme/static/src/scss/abstracts/odoo_primary_variables.scss',
        ],
        'web.assets_backend': [
            '/ks_curved_backend_theme/static/src/scss/abstracts/variables.scss',
            '/ks_curved_backend_theme/static/src/scss/base/fonts.scss',
            '/ks_curved_backend_theme/static/src/scss/base/default.scss',
            '/ks_curved_backend_theme/static/src/scss/base/animation.scss',
            '/ks_curved_backend_theme/static/src/scss/base/forms.scss',
            '/ks_curved_backend_theme/static/src/scss/base/fields.scss',
            '/ks_curved_backend_theme/static/src/scss/abstracts/mixins.scss',
            '/ks_curved_backend_theme/static/src/scss/abstracts/placeholder.scss',
            '/ks_curved_backend_theme/static/src/scss/components/buttons.scss',
            '/ks_curved_backend_theme/static/src/scss/components/color_theme.scss',
            '/ks_curved_backend_theme/static/src/scss/components/tabs.scss',
            '/ks_curved_backend_theme/static/src/scss/components/table.scss',
            '/ks_curved_backend_theme/static/src/scss/components/form-control.scss',
            '/ks_curved_backend_theme/static/src/scss/components/checkbox.scss',
            '/ks_curved_backend_theme/static/src/scss/components/loaders.scss',
            '/ks_curved_backend_theme/static/src/scss/components/Breadcrumb.scss',
            '/ks_curved_backend_theme/static/src/scss/layout/header.scss',
            '/ks_curved_backend_theme/static/src/scss/layout/apps-drawer.scss',
            '/ks_curved_backend_theme/static/src/scss/layout/ks_quick_settings.scss',
            '/ks_curved_backend_theme/static/src/scss/layout/sidebar.scss',
            '/ks_curved_backend_theme/static/src/scss/layout/bookmark.scss',
            '/ks_curved_backend_theme/static/src/scss/layout/ks_control_panel.scss',
            '/ks_curved_backend_theme/static/src/scss/layout/ks_form_view.scss',
            '/ks_curved_backend_theme/static/src/scss/layout/ks_view.scss',
            '/ks_curved_backend_theme/static/src/scss/layout/ks_vertical_menus.scss',
            '/ks_curved_backend_theme/static/src/scss/responsive/ipad_responsive.scss',
            '/ks_curved_backend_theme/static/src/scss/responsive/phone_responsive.scss',
            '/ks_curved_backend_theme/static/src/scss/pages/discuss.scss',
            '/ks_curved_backend_theme/static/src/scss/pages/calendar.scss',
            '/ks_curved_backend_theme/static/src/scss/pages/all_apps.scss',
            '/ks_curved_backend_theme/static/src/lib/owl.carousel.min.css',

            # js assets
            '/ks_curved_backend_theme/static/src/Components/ks_dropdown_menu.js',
            '/ks_curved_backend_theme/static/src/Components/Ks_custom_action_menu.js',
            '/ks_curved_backend_theme/static/src/js/Ks_control_panel_inherit.js',
            '/ks_curved_backend_theme/static/src/js/ks_searchbar.js',
            '/ks_curved_backend_theme/static/src/js/Ks_controlpanel_view.js',
            '/ks_curved_backend_theme/static/src/js/splitview/KsAbstractControllerInherit.js',
            '/ks_curved_backend_theme/static/src/js/widgets/ksListDocumentViewer.js',
            # '/ks_curved_backend_theme/static/src/js/splitview/KsActionManagerInherit.js',
            '/ks_curved_backend_theme/static/src/js/KsWebFrameWork_inherit.js',
            '/ks_curved_backend_theme/static/src/js/ks_app_sidebar.js',
            '/ks_curved_backend_theme/static/src/js/ks_left_sidebar_panel.js',
            '/ks_curved_backend_theme/static/src/js/ks_switch_language.js',
            '/ks_curved_backend_theme/static/src/js/ks_darkmode_toggle.js',
            '/ks_curved_backend_theme/static/src/js/ks_bookmarks_menu.js',
            '/ks_curved_backend_theme/static/src/js/ks_quick_settings_widget.js',
            '/ks_curved_backend_theme/static/src/js/ks_appsmenu.js',
            '/ks_curved_backend_theme/static/src/js/ks_fullscreen.js',
            '/ks_curved_backend_theme/static/src/js/ks_search_panel.js',
            '/ks_curved_backend_theme/static/src/js/views/list/ks_list_renderer.js',
            '/ks_curved_backend_theme/static/src/js/views/form/ks_form_render.js',
            '/ks_curved_backend_theme/static/src/js/ks_global_config_widget.js',
            '/ks_curved_backend_theme/static/src/js/ks_company_config_widget.js',
            '/ks_curved_backend_theme/static/src/js/ks_appdrawer_edit.js',
            '/ks_curved_backend_theme/static/src/js/ks_click_to_edit.js',
            '/ks_curved_backend_theme/static/src/js/ks_abstract_web_client.js',
            '/ks_curved_backend_theme/static/src/js/ks_data_manager.js',
            '/ks_curved_backend_theme/static/src/js/ks_zoom_btn_visibility.js',
            '/ks_curved_backend_theme/static/src/js/ks_calendar_view.js',
            '/ks_curved_backend_theme/static/src/js/ks_relation_fields.js',
            '/ks_curved_backend_theme/static/src/js/views/form/ks_form_controller.js',
            '/ks_curved_backend_theme/static/src/js/views/list/ks_list_controller.js',
            '/ks_curved_backend_theme/static/src/js/ksAbstractController.js',
            '/ks_curved_backend_theme/static/src/js/views/kanban/ks_kanban_controller_inherit.js',
            #'/ks_curved_backend_theme/static/src/js/views/graph/ks_graph_controller_inherit.js',
            # '/ks_curved_backend_theme/static/src/js/views/pivot/ks_pivot_controller_inherit.js',
            '/ks_curved_backend_theme/static/src/js/views/calendar/ks_calendar_controller_inherit.js',
            '/ks_curved_backend_theme/static/src/lib/owl.carousel.min.js',
            '/ks_curved_backend_theme/static/src/js/app.js',
            '/ks_curved_backend_theme/static/src/js/sw.js',
        ],
        'web.assets_frontend': [
            '/ks_curved_backend_theme/static/src/scss/pages/ks_login.scss',
            '/ks_curved_backend_theme/static/src/scss/base/fonts.scss',
            '/ks_curved_backend_theme/static/src/scss/weevy/weevy_assets_frontend.scss',
            ('after', '/portal/static/src/scss/portal.scss', '/ks_curved_backend_theme/static/src/scss/weevy/weevy_assets_portal.scss'),
            '/ks_curved_backend_theme/static/src/scss/weevy/weevy_overwrite_primary_vars.scss',
        ],

    },

    "application": True,
    "installable": True,
}
