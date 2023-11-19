import h5py

def SaveH5(filename, data_array,dataset):
    try:
        with h5py.File(filename, 'a') as file:
            dataset = file.create_dataset(f"{dataset}",data=data_array)
    except Exception as e:
        print(f"Error: {e}")
