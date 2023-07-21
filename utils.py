import shutil, os
from constants import IMAGES_FOLDER

class SendZipOutput:

    def __init__(self, query: str):
        self.query = query
    

    def zip_folder(self,source_folder, output_zip_file):
        try:
            shutil.make_archive(output_zip_file, 'zip', source_folder)
            print(f"Successfully created '{output_zip_file}'.")
        except Exception as e:
            print(f"Error creating zip archive: {e}")

    def makezip(self):

        try:
            searched_images_folder = self.query.strip().lower()
            source = os.path.join(
                os.getcwd(),
                IMAGES_FOLDER,
                searched_images_folder
                
                )
            
            print("source",source)
            
            self.zip_folder(
                source_folder=source,
                output_zip_file= searched_images_folder
            )

            

        except Exception as e:
            print(f"Error creating zip archive: {e}")

            
            
            


