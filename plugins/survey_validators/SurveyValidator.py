from service_catalog.forms import SurveyValidator
from profiles.models.scope import AbstractScope
from profiles.models.quota import Quota 

class ValidatorForVM(SurveyValidator):
    def validate_survey(self): 
        print("\n\n\n\n\n  ------------------------------------------------------------")
        # {'request_comment': '', 'pb_vmaas_ostype': 'linux', 'pb_vmaas_env': 'development', 'pb_vmaas_linux_distro': 'Rocky 9.1', 'pb_vmaas_tshirt_size': 'small'}
        try: 
            instance = self.instance
            print(instance.name)
            print(instance.quota_scope) 
            selected_scope_object = AbstractScope.objects.get(name=instance.quota_scope) 
            scope_id = selected_scope_object.id 
            quota_object_for_CPU = Quota.objects.filter(scope_id=scope_id , attribute_definition_id =2).first()
            quota_object_for_RAM = Quota.objects.filter(scope_id=scope_id , attribute_definition_id =3).first()
            quota_object_for_STORAGE = Quota.objects.filter(scope_id=scope_id , attribute_definition_id =4).first()
            # limit set for attributes:
            cpu_limit = quota_object_for_CPU.limit
            ram_limit = quota_object_for_RAM.limit
            storage_limit = quota_object_for_STORAGE.limit 
            print(f"cpu_limit : {cpu_limit} , ram_limit : {ram_limit} , storage_limit : {storage_limit}")
            
             # available  for attributes:
            cpu_available = quota_object_for_CPU.available
            ram_available = quota_object_for_RAM.available
            storage_available = quota_object_for_STORAGE.available  
            print(f"cpu_available : {cpu_available} , ram_available : {ram_available} , storage_available : {storage_available}")
            
             # consumed  for attributes:
            cpu_consumed = quota_object_for_CPU.consumed
            ram_consumed = quota_object_for_RAM.consumed
            storage_consumed = quota_object_for_STORAGE.consumed 
            print(f"cpu_consumed : {cpu_consumed} , ram_consumed : {ram_consumed} , storage_consumed : {storage_consumed}")
            
            #----------------------------------------------------------------
            survey_dict = self.survey
            vm_size = survey_dict.get('pb_vmaas_tshirt_size') 
            size = vm_size.split(" ")[0].lower()
            
            cpu , ram , disk = self.get_specifications(size) 
            
            if cpu_available < cpu or ram_available < ram or storage_available < disk:
                self.fail(f"Your team :{instance.quota_scope}, quota limits set for VMware VMaaS service is exhausted, please get in touch with your Squest and Automation admins to increase the quota limits")
            else: 
                print("Validators for tshirt size Passed !")
            
        except Exception as e : 
            print(str(e))

    def get_specifications(self, size):
        if size == "small":
            return 2, 2, 40
        elif size == "medium":
            return 2, 4, 80
        elif size == "large":
            return 4, 6, 100
        else:
            raise ValueError("Invalid size specified. Please choose among 'small', 'medium', or 'large'.")
                   
class ValidatorForOSDistro(SurveyValidator):  
    def validate_survey(self):
        try:
            survey_dict = self.survey 
            os_distro = survey_dict.get('pb_vmaas_os_distro') 
            os_type = survey_dict.get('pb_vmaas_ostype') 
            
            if os_type == 'Windows' and 'windows' not in os_distro.lower(): 
                self.fail(" Invalid os distro selected! - Please select valid os distro for os Type: Windows")
            elif os_type == 'Linux' and 'windows' in os_distro.lower():  
               self.fail(" Invalid os distro selected! - Please select valid os distro for os Type: linux")      
            else: 
               print("Validators passed!")                    
        except Exception as e : 
            print(str(e))
        
             