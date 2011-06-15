from mezzanine.conf import register_setting

register_setting(
        name="MAINTENANCE_ON",
        description="Configuration of the maintenance mode, True closes the site.",
        editable=True,
        default=False,
        )

