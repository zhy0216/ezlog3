

''' site model '''

class Site(db.Document):
    site_version            = db.DecimalField(required=True, precision=2)
    model_version           = db.DecimalField(required=True, precision=2)


    meta = {
        'allow_inheritance': False,
        'index_types': False,
    }


class UploadFile(db.Document):
    file_name               = db.StringField(required=True)
    file_type               = db.StringField(required=True)

