import uproot
import awkward as ak

# def concatenate_and_copy_ttrees(root_file_path, tree_names_to_concatenate, output_file_path, output_tree_name):
def concatenate_and_copy_ttrees(root_file_path, output_file_path):
    # Open the input ROOT file
    with uproot.open(root_file_path) as input_file:

        # get list of tree names
        trees = input_file.keys()
        # get list of suffixes = variations = nominal, systematics, ...
        suffixes = [i.split("emu_WW")[-1].strip(";1")[1:] for i in trees if "WW" in i]
        # list of sample to concatenate for each suffix
        samplesToConcat = ["WW", "Zee", "Zmumu", "Ztautau"]
        
        # make place holders
        concatenated_arrays = []
        output_tree_names = []
        list_of_concatenated_trees = []
        for suffix in suffixes:

            # get list of trees to concatenate
            tree_names_to_concatenate = []
            for tree_name in trees:
                if suffix in tree_name and any(sample in tree_name for sample in samplesToConcat):
                    tree_names_to_concatenate.append(tree_name)

            # Read the TTrees to be concatenated into a list of Awkward Arrays
            arrays_to_concatenate = [input_file[tree_name].arrays(library="ak") for tree_name in tree_names_to_concatenate]

            # Concatenate the Awkward Arrays
            concatenated_array = ak.concatenate(arrays_to_concatenate, axis=0)

            # store them
            output_tree_names.append(f"emu_WWandZll_{suffix}")
            concatenated_arrays.append(concatenated_array)
            list_of_concatenated_trees += tree_names_to_concatenate


        print(len(suffixes), len(samplesToConcat), len(list_of_concatenated_trees))
        print(list_of_concatenated_trees)
        
        # Read the TTrees to be concatenated into a list of Awkward Arrays
        # arrays_to_concatenate = [input_file[tree_name].arrays(library="ak") for tree_name in tree_names_to_concatenate]
        
        # Concatenate the Awkward Arrays
        # concatenated_array = ak.concatenate(arrays_to_concatenate, axis=0)
        
        # Open the output ROOT file
        with uproot.recreate(output_file_path) as output_file:

            # write the concatenated trees
            for output_tree_name, concatenated_array in zip(output_tree_names, concatenated_arrays):
                # Write the concatenated TTree to the output file
                output_file[output_tree_name] = concatenated_array
            
            # Copy all other TTrees to the output file
            for tree_name, tree in input_file.items():
                if tree_name not in list_of_concatenated_trees:
                    # remove the ;1 that for some reason root adds
                    new_tree_name = tree_name.strip(";1")
                    output_file[new_tree_name] = tree.arrays(library="ak")
                else:
                    print(tree_name)
                    
if __name__ == "__main__":

    # Example usage
    root_file_path = "/home/abadea/analysis/ttbarPbPb/AnalysisTop/run/TRExFitter/input/PbPbv45/hists.root"
    tree_names_to_concatenate = ["emu_WW_nominal", "emu_Zee_nominal", "emu_Zmumu_nominal", "emu_Ztautau_nominal"]  # List of TTree names to concatenate
    output_file_path = "output.root"
    output_tree_name = "emu_WWandZll_nominal"

    # concatenate_and_copy_ttrees(root_file_path, tree_names_to_concatenate, output_file_path, output_tree_name)
    concatenate_and_copy_ttrees(root_file_path, output_file_path)
