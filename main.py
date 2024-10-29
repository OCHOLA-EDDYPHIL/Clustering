import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


def main():
    # Load the dataset
    file_path = 'Dataset Group 1.xlsx'
    xls = pd.ExcelFile(file_path)
    data = pd.read_excel(xls, sheet_name='Sheet1')

    # Select relevant columns for clustering
    data_subset = data[['Usage (MB)', 'Network Type', 'Location', 'Application Type', 'Connection Quality']].copy()

    # Encode categorical variables
    label_encoders = {col: LabelEncoder() for col in data_subset.select_dtypes(include='object').columns}
    for col, le in label_encoders.items():
        data_subset.loc[:, col] = le.fit_transform(data_subset[col])

    # Normalize the data
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data_subset)

    # Plot dendrograms for 'single', 'complete', and 'average' linkage methods
    for method in ['single', 'complete', 'average']:
        plot_dendrogram(data_scaled, method)


def plot_dendrogram(data, method):
    plt.figure(figsize=(10, 6))
    linkage_matrix = linkage(data, method=method)
    dendrogram(linkage_matrix, truncate_mode='lastp', p=10, leaf_rotation=45, leaf_font_size=10)
    plt.title(f'Hierarchical Clustering Dendrogram ({method} linkage)')
    plt.xlabel('Sample index or (cluster size)')
    plt.ylabel('Distance')
    plt.show()


if __name__ == "__main__":
    main()
