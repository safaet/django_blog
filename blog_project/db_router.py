class MembersDBRouter:
    """
    A database router to direct queries for the 'members' app to 'members.sqlite'.
    All other apps use the default database.
    """

    def db_for_read(self, model, **hints):
        """Read operations"""
        if model._meta.app_label == 'members':
            return 'members_db'  # Use members.sqlite
        return 'default'  # Use db.sqlite3

    def db_for_write(self, model, **hints):
        """Write operations"""
        if model._meta.app_label == 'members':
            return 'members_db'  # Use members.sqlite
        return 'default'  # Use db.sqlite3

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Migration control"""
        if app_label == 'members':
            return db == 'members_db'
        return db == 'default'
