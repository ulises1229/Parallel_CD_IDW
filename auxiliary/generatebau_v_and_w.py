# -*- coding: utf-8 -*-

#Author: Ulises Olivares
#uolivares@unam.mx
# Nov 3, 2022

import pandas as pd
import numpy as np

class ImportDemmand():

    
    def convertDemmand(self, name):
        demmand = pd.read_csv(name, sep=",")
        
        # Filer walking registers
        walking = demmand.filter(regex=rf"ID|fw_w")
        
        walking.to_csv(name.replace(".csv", "_walking.csv"), index=False)


        # Drop first column
        #deleted_column = df.pop(df.columns[0])

        #Filter vehicle registers
        fw_v = demmand.filter(regex=rf"fw_v")
        ch_v = demmand.filter(regex=rf"ch_v")

        # rename variables for the two datas
        ch_v.columns = fw_v.columns
        
        # marge the two DF
        vehicle = fw_v.add(ch_v,fill_value = 0)

        IDs = demmand.filter(regex=rf"ID")

        vehicle.insert(0, "ID", IDs)
        vehicle.to_csv(name.replace(".csv", "_vehicle.csv"), index=False)

        
        
        
        
        


def main():
    # Name of demmand file 
    name = "BaU_fwch.csv"
    objImp = ImportDemmand()
    objImp.convertDemmand(name)

if __name__ == "__main__":
    main()
