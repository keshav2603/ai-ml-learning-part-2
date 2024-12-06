# class emp:
#     company_name ="apple"
#     def __init__(self,name):
#         self.name =name

#     @classmethod
#     def strfun(cls, str):
#         cls.company_name=str

class ok:
    def __call__(self):
        print("hello world")

ap= ok()
ap()