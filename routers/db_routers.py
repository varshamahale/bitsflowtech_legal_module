class CollappRouter:
    route_app_labels = {'collapp','auth', 'contenttypes', 'sessions', 'admin'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'collapp_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'collapp_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'collapp_db'
        return None

# class Vegeta:
#     route_app_labels = {'vegeta'}

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'vegeta_db'
#         return None

#     def db_for_write(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'vegeta_db'
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         if app_label in self.route_app_labels:
#             return db == 'vegeta_db'
#         return None


class CommunicationRouter:
    route_app_labels = {'communication'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'communication_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'communication_db'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'communication_db'
        return None



# Referrence :
# Cros-Relation DB & foriegn-key patch
# https://stackoverflow.com/questions/23268895/cross-database-foreign-key-error