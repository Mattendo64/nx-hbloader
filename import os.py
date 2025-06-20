import os
import subprocess

def nsp_to_cxi(nsp_path, output_dir, title_key):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Step 1: Extract NSP contents
    print("Extracting NSP...")
    subprocess.run([
        "hactool", "-x",
        "--titlekey", title_key,
        "--outdir", output_dir,
        nsp_path
    ], check=True)
    
    # Step 2: Find the main NCA (assuming the largest or a specific one)
    nca_files = [f for f in os.listdir(output_dir) if f.endswith(".nca")]
    if not nca_files:
        print("No NCA files found.")
        return
    
    # For simplicity, pick the first NCA (or add logic to select the main one)
    nca_path = os.path.join(output_dir, nca_files[0])
    print(f"Found NCA: {nca_path}")
    
    # Step 3: Extract the CXI from the NCA
    print("Extracting CXI from NCA...")
    subprocess.run([
        "hactool", "--section=0",
        "--outdir", output_dir,
        nca_path
    ], check=True)
    
    # The CXI should now be in the output directory
    for file in os.listdir(output_dir):
        if file.endswith(".cxi"):
            print(f"CXI extracted: {os.path.join(output_dir, file)}")
            return os.path.join(output_dir, file)

# Usage example:
if __name__ == "__main__":
    nsp_file = "your_game.nsp"
    output_folder = "extracted"
    title_key = "YOUR_TITLE_KEY"  # Replace with your actual key
    nsp_to_cxi(nsp_file, output_folder, title_key)
   try:
    subprocess.run([...], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error during subprocess execution: {e}")
    return
 