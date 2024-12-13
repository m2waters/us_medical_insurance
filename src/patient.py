

class patient:

    def __init__(self, 
                 patient_uuid,
                 age, 
                 sex, 
                 bmi, 
                 num_of_children, 
                 smoker, 
                 region, 
                 charges,                
            ):
        
        self.uuid = patient_uuid
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.num_of_children = num_of_children
        self.smoker = smoker
        self.region = region
        self.charges = charges
