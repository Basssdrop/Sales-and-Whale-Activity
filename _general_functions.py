import h5py

def SaveH5(filename, data_array,dataset):
    try:
        with h5py.File(filename, 'a') as file:
            dataset = file.create_dataset(f"{dataset}",data=data_array)
    except Exception as e:
        print(f"Error: {e}")

def LoadH5(file_path, dataset_name):
    try:
        with h5py.File(file_path, 'r') as file:
            # Check if the dataset exists
            if dataset_name not in file:
                raise KeyError(f"Dataset '{dataset_name}' not found in the HDF5 file.")

            # Read the dataset into a NumPy array
            dataset = file[dataset_name][...]
            return dataset
    except Exception as e:
        print(f"Error reading HDF5 dataset: {str(e)}")
        return None
