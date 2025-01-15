import pandas as pd
import os

class CSVDataProcessor():
    
    def __init__(self, output, path_sist, path_tsi, path_weather, sec_vis=False):
        self.output = output
        self.pre_sist = path_sist
        self.pre_tsi = path_tsi 
        self.pre_weather = path_weather
        
 # This might be an input variable but for now, we will include the dict inside the class.
        self.nomenclatura = {
                "C2": "Corrida2",
                "C3": "Corrida3",
                "C4": "Corrida4",
                "C5": "Corrida5",
                "C6": "Corrida6",
                "C7": "Corrida7",
                "C8": "Corrida8",
                "C9": "Corrida9",
                "C10": "Corrida10",
                "C11": "Corrida11",
                "C12": "Corrida12",
                "C13": "Corrida13",
                "C14": "Corrida14",
                "C15": "Corrida15",
                "C16" : "Corrida16",
                "C17" : "Corrida17",
                "C18": "Corrida18",
                "C19": "Corrida19",
                "C20" : "Corrida20",
                "C21": "Corrida21",
                "C22" : "Corrida22",
                "C23" : "Corrida23",
                "C24" : "Corrida24",
                "C25": "Corrida25",
                "C26": "Corrida26",
                "C27": "Corrida27",
                "C28" : "Corrida28",
                "C51": "Corrida51",
                "C52" :"Corrida52",
                "C53": "Corrida53",
                "C54" : "Corrida54",
                "C55" : "Corrida55", 
                "C56" : "Corrida56",
                "С63": "Corrida63",
                "С64" : "Corrida64",
                "С66": "Corrida66",
                "C67" : "Corrida67",
                "C68" : "Corrida68",
                "C80" : "Corrida80",
                "C81": "Corrida81",
                "C84" : "Corrida84",
                
                }
        


    def process_csv_files(self):
        """Main code to process data from different sources."""
        excel_writer = None  # Initialize excel_writer outside the try block
        try:
            for folder in os.listdir(self.pre_sist):
                # Constants
                df_ranged = None  # Initialize df_ranged inside the loop
                cleaned_dataframes = []  # List of dataframes cleaned and ready to concat them.
                excel_writer = None  # Initialize excel_writer

                pre_path = os.path.join(self.pre_sist, folder)
                folder_tsi = os.listdir(self.pre_tsi)
                self.df_analysis = DataAnalizer()

                csv_files = [file for file in os.listdir(pre_path) if file.endswith('.csv')]

            
                excel_writer = pd.ExcelWriter(os.path.join(self.output, folder, f"{folder}.xlsx"))

                # Initialize HDF5 file
                with pd.HDFStore(f'.h5') as store:

                    for csv_file in csv_files:
                        csv_name = csv_file.split("_")[2]

                        # Read the df according to the above, no need for sheet selector.
                        df = pd.read_csv(os.path.join(pre_path, csv_file))

                        # Load the df into the Data Analyzer class to merge all the variables in a df.
                        if df_ranged is None:
                            df_ranged = self.df_analysis.get_times_df(df)
                        df = self.df_analysis.main_workflow(df, df_ranged)
                        cleaned_dataframes.append(df)

                        
                        print(f"Data from {csv_name} loaded")
                        # Save to excel if required 
                        df.to_excel(excel_writer, sheet_name=csv_name, index=False)

                        # Save the DataFrame to HDF5 with a unique key (e.g., 'csv_name_df')
                        store[csv_name + '_df'] = df

                    for folder_number in folder_tsi:
                        if folder_number == "3_Maniobrabilidad":
                            pass 
                        else:
                            file_tsi_selector = f"{str(folder.split('_')[0])}"
                            sheet_selector = str(self.nomenclatura[folder.split('_')[1]])
                            filename = os.path.join(folder_number, f'{file_tsi_selector}.xlsx')

                            tsi_path_ready = os.path.join(self.pre_tsi, filename)
                            print(tsi_path_ready)

                            if df_ranged is None:
                                df_ranged = self.df_analysis.get_times_df(df)
                            df = self.df_analysis.main_workflow(df, df_ranged)
                            cleaned_dataframes.append(df)

                            df = self.df_analysis.clean_df(df, csv_name)
                            df.to_pickle(os.path.join(self.output, f"{folder}.pkl"))

                            df.to_excel(excel_writer, sheet_name=folder_number, index=False)

                # Close the HDF5 file

                
                excel_writer.save()

                processed_dataframes = pd.concat(cleaned_dataframes, ignore_index=False, axis=1)  # Axis=1 as all the df will have the same index
                processed_dataframes.to_pickle(os.path.join(self.output, f"{folder}.pkl"))

        except Exception as e:
            print(f"Error processing CSV: {str(e)}")
        finally:
            if excel_writer:
                excel_writer.close()




class YourDataProcessorClass:
    def __init__(self):
        self.df_ranged = None
        self.df_analysis = DataAnalizer()
        self.excel_writer = None

    def function_selector(self, file_path):
        # Determine whether the file is CSV or Excel and call the appropriate function
        if file_path.endswith('.csv'):
            self.process_csv(file_path)
        elif file_path.endswith('.xlsx'):
            self.process_excel(file_path)

    def process_csv(self, file_path):
        # Read CSV, process data, and save
        df = pd.read_csv(file_path)
        if self.df_ranged is None:
            self.df_ranged = self.df_analysis.get_times_df(df)
        df = self.df_analysis.main_workflow(df, self.df_ranged)
        self.save_pickle(df, self.output, 'output_filename')
        # Other processing specific to CSV files

    def process_excel(self, file_path):
        # Read Excel, process data, and save
        df = pd.read_excel(file_path)
        if self.df_ranged is None:
            self.df_ranged = self.df_analysis.get_times_df(df)
        df = self.df_analysis.main_workflow(df, self.df_ranged)
        self.save_pickle(df, self.output, 'output_filename')
        # Other processing specific to Excel files


    @pickle
    def save_pickle(self, dataframe, path, name):
        dataframe.to_pickle(os.path.join(path, f"{name}.pkl"))

    def process_files_in_directory(self, directory_path):
        # Process all files in a directory
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)
            self.function_selector(file_path)

# Usage:
processor = YourDataProcessorClass()
processor.process_files_in_directory('/path/to/directory')