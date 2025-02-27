import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore


def get_general_properties(data: pd.DataFrame):
    """
    Extracts general properties of the dataset.
    """
    return {
        "Number of Rows": data.shape[0],
        "Number of Columns": data.shape[1],
        "Columns": list(data.columns),
        "Missing Values": data.isnull().sum().to_dict(),
        "Duplicated Rows": data.duplicated().sum(),
        "Data Types": data.dtypes.to_dict(),
    }


def describe_numerical(data: pd.DataFrame):
    """
    Describes numerical variables in the dataset.
    """
    numerical_vars = data.select_dtypes(include=["int64", "float64"]).columns
    return data[numerical_vars].describe().to_dict()


def save_catalog_as_tsv(catalog: dict, file_path: str):
    """
    Saves the catalog dictionary as a TSV file.

    Parameters:
    - catalog (dict): The dictionary containing dataset properties.
    - file_path (str): The path to save the TSV file.
    """
    flattened_catalog = []

    for key, value in catalog.items():
        if isinstance(
            value, dict
        ):  # Handle nested dictionaries (e.g., Missing Values, Data Types)
            for sub_key, sub_value in value.items():
                flattened_catalog.append([f"{key} - {sub_key}", sub_value])
        elif isinstance(value, list):  # Handle lists (e.g., Column names)
            flattened_catalog.append([key, ", ".join(map(str, value))])
        else:  # Handle scalar values
            flattened_catalog.append([key, value])

    df_catalog = pd.DataFrame(flattened_catalog, columns=["Property", "Value"])
    df_catalog.to_csv(file_path, sep="\t", index=False)


def describe_categorical(data: pd.DataFrame):
    """
    Describes categorical variables in the dataset.
    """
    categorical_vars = data.select_dtypes(include=["object", "category"]).columns
    return {var: data[var].value_counts().to_dict() for var in categorical_vars}


def get_correlation_matrix(data: pd.DataFrame):
    """
    Computes the correlation matrix for numerical variables.
    """
    numerical_vars = data.select_dtypes(include=["int64", "float64"]).columns
    return data[numerical_vars].corr()


def detect_outliers(data: pd.DataFrame, column: str, z_thresh: float = 3):
    """
    Detects outliers in a specified column using the Z-score method.
    """
    z_scores = zscore(data[column].dropna())
    return data.loc[abs(z_scores) > z_thresh]


def plot_target_distribution(data: pd.DataFrame, target: str):
    """
    Plots the distribution of the target variable.
    """
    plt.figure(figsize=(8, 5))
    sns.countplot(x=target, data=data, palette="viridis")
    plt.title(f"Distribution of Target Variable: {target}")
    plt.xlabel(target)
    plt.ylabel("Count")
    plt.show()


def plot_numerical_distributions(data: pd.DataFrame, numerical_vars: list):
    """
    Plots histograms for numerical variables.
    """
    data[numerical_vars].hist(
        bins=20, figsize=(15, 10), color="teal", edgecolor="black"
    )
    plt.suptitle("Distributions of Numerical Variables", size=16)
    plt.show()


def plot_categorical_distributions(data: pd.DataFrame, categorical_vars: list):
    """
    Plots bar charts for categorical variables.
    """
    for var in categorical_vars:
        plt.figure(figsize=(8, 5))
        sns.countplot(
            y=var, data=data, palette="crest", order=data[var].value_counts().index
        )
        plt.title(f"Distribution of {var}")
        plt.xlabel("Count")
        plt.ylabel(var)
        plt.show()


def plot_pairwise_relationships(
    data: pd.DataFrame, numerical_vars: list, target: str = None
):
    """
    Plots pairwise relationships between numerical variables.
    """
    sns.pairplot(
        data[numerical_vars + ([target] if target else [])],
        hue=target,
        palette="coolwarm",
    )
    plt.suptitle("Pairwise Relationships", size=16)
    plt.show()


def plot_correlation_matrix(data: pd.DataFrame, numerical_vars: list):
    """
    Visualizes the correlation matrix for numerical variables.
    """
    plt.figure(figsize=(10, 8))
    correlation_matrix = data[numerical_vars].corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Correlation Matrix")
    plt.show()


def plot_missing_data(data: pd.DataFrame):
    """
    Visualizes missing data patterns.
    """
    plt.figure(figsize=(12, 6))
    sns.heatmap(data.isnull(), cbar=False, cmap="viridis", yticklabels=False)
    plt.title("Missing Data Heatmap")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.show()


def plot_outlier_detection(data: pd.DataFrame, column: str):
    """
    Visualizes outliers in a specified numerical variable using a boxplot.
    """
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=column, data=data, palette="Set2")
    plt.title(f"Outlier Detection for {column}")
    plt.xlabel(column)
    plt.show()


def fill_nas_by_median(data: pd.DataFrame, column: str):
    """
    Leakage : Imputation Fill na's in a column by computing the median
    """
    data[column].fillna(data[column].median(), inplace=True)
