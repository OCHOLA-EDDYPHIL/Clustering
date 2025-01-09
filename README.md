``` bash
   pip install pandas scikit-learn matplotlib scipy
```

## File Structure

- **main.py**: The main script containing the data preprocessing, clustering, and visualization functions.
- **Dataset Group 1.xlsx**: The dataset file used for clustering analysis.

### Dataset

The dataset should contain the following columns:

- `Usage (MB)` (Numerical): Data usage in megabytes.
- `Network Type` (Categorical): Type of network used.
- `Location` (Categorical): Geographic location.
- `Application Type` (Categorical): Type of application accessed.
- `Connection Quality` (Categorical): Quality of the connection.

Ensure that the file `Dataset Group 1.xlsx` is in the same directory as the script.

## How It Works

1. **Load Dataset**: The given Excel file is read using the `pandas` library.
2. **Select Relevant Columns**: Only the necessary columns for clustering are used.
3. **Encode Categorical Variables**: Categorical columns are label-encoded to replace text with numerical values.
4. **Normalize the Data**: All columns are normalized using `StandardScaler` for better clustering performance.
5. **Perform Hierarchical Clustering**: Clustering is performed using three linkage methods:
    - `Single`
    - `Complete`
    - `Average`

6. **Plot Dendrograms**: Dendrograms are plotted for each linkage method to visualize how samples are grouped.

## Running the Project

To run the analysis, follow these steps:

1. Clone the repository to your local machine.
2. Place the `Dataset Group 1.xlsx` file in the project root directory.
3. Run the `main.py` script:

``` bash
    python main.py
```

This will generate dendrograms for each of the three linkage methods (`single`, `complete`, and `average`). The
dendrograms help visualize the clustering process.

## Example Output

The script outputs dendrogram plots like the following:

- A plot showcasing the hierarchical relationships of the clusters.
- Separate plots for each of the linkage methods (`single`, `complete`, and `average`).

## License

This project is for educational and demonstration purposes. Use the code as you see fit for learning purposes.
