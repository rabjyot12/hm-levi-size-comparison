import pandas as pd

hm_tops = pd.read_csv("D:\\Projects\\hm-levi-size-comparison\\data\\hm_tops.csv")
#print(hm_tops)
#print(hm_tops.shape)
#print(hm_tops.info())
hm_bottoms = pd.read_csv("D:\\Projects\\hm-levi-size-comparison\\data\\hm_bottoms.csv")

levis_tops = pd.read_csv("D:\\Projects\\hm-levi-size-comparison\\data\\levis_tops.csv")
levis_bottoms = pd.read_csv("D:\\Projects\\hm-levi-size-comparison\\data\\levis_bottoms.csv")

'''print("H&M Tops:", hm_tops.shape)
print("Levi's Tops:", levis_tops.shape)
print("H&M Bottoms:", hm_bottoms.shape)
print("Levi's Bottoms:", levis_bottoms.shape)'''

'''
print("\nH&M Tops Missing Values:")
print(hm_tops.isnull().sum())

print("\nLevi's Tops Missing Values:")
print(levis_tops.isnull().sum())

print("\nH&M Bottoms Missing Values:")
print(hm_bottoms.isnull().sum())

print("\nLevi's Bottoms Missing Values:")
print(levis_bottoms.isnull().sum())'''


#check range 
def check_ranges(df, min_column):
    for min_col in min_column:
        max_col = min_col.replace("_min_", "_max_")
        invalid = df[df[min_col] > df[max_col]]
        if len(invalid) == 0:
            print(f"{min_col}: all ranges are valid") 
        else:
            print(f"{min_col}: found invalid ranges")
            print(invalid)

'''
print("\nChecking H&M Tops ranges:")

check_ranges(
    hm_tops,
    [
        "chest_min_cm",
        "waist_min_cm",
        "neckline_min_cm",
        "arm_length_min_cm"
    ]
)
'''

'''
print("\nChecking Levi's tops:")
check_ranges(
    levis_tops,
    [
        "neck_min_cm",
        "chest_min_cm",
        "waist_min_cm",
        "seat_min_cm"
    ]
)

print("\nChecking H&M bottoms:")
check_ranges(
    hm_bottoms,
    [
        "waist_min_cm",
        "hip_min_cm",
        "length_30_min_cm",
        "length_32_min_cm",
        "length_34_min_cm"
    ]
)

print("\nChecking Levi's bottoms:")
check_ranges(
    levis_bottoms,
    [
        "waist_min_cm",
        "seat_min_cm",
        "thigh_min_cm"
    ]
)
'''


#this calculates midpoint between min and max columns for a given dataframe
def calculate_midpoint(df, min_col, max_col):
    return (df[min_col] + df[max_col]) / 2

hm_tops["chest_mid_cm"] = calculate_midpoint(
    hm_tops,
    "chest_min_cm",
    "chest_max_cm"
)

levis_tops["chest_mid_cm"] = calculate_midpoint(
    levis_tops,
    "chest_min_cm",
    "chest_max_cm"
)

'''
print("\nH&M chest:")
print(hm_tops[["size", "chest_min_cm", "chest_max_cm", "chest_mid_cm"]])

print("\nLevi's chest:")
print(levis_tops[["size", "chest_min_cm", "chest_max_cm", "chest_mid_cm"]])
'''


#this merges the two dataframes on the size column and calculates the difference in chest measurements between H&M and Levi's
common_tops = pd.merge(
    hm_tops,
    levis_tops,
    on="size",
    suffixes=("_hm", "_levis")
)

'''
print("\nCommon top sizes:")
print(common_tops)
'''

#this calculates the difference in chest measurements between H&M and Levi's
common_tops["chest_mid_difference_cm"] = (
    common_tops["chest_mid_cm_levis"]
    - common_tops["chest_mid_cm_hm"]
)

'''
print(
    common_tops[
        ["size", "chest_mid_cm_hm",
         "chest_mid_cm_levis",
         "chest_mid_difference_cm"]
    ]
)
'''

#this calculates the overlap in chest measurements between H&M and Levi's
common_tops["overlap_min"] = common_tops[
    ["chest_min_cm_hm", "chest_min_cm_levis"]
].max(axis=1)

common_tops["overlap_max"] = common_tops[
    ["chest_max_cm_hm", "chest_max_cm_levis"]
].min(axis=1)

common_tops["chest_overlap_cm"] = (
    common_tops["overlap_max"] - common_tops["overlap_min"]
)
common_tops.loc[common_tops["chest_overlap_cm"] < 0, "chest_overlap_cm"] = 0

'''
print(
    common_tops[
        [
            "size",
            "chest_min_cm_hm",
            "chest_max_cm_hm",
            "chest_min_cm_levis",
            "chest_max_cm_levis",
            "chest_overlap_cm"
        ]
    ]
)
'''

#this calculates the range of chest measurements for H&M
common_tops["hm_chest_range_cm"] = (
    common_tops["chest_max_cm_hm"] -
    common_tops["chest_min_cm_hm"]
)

#this calculates the percentage of overlap in chest measurements between H&M and Levi's
common_tops["chest_overlap_percent"] = (
    common_tops["chest_overlap_cm"] /
    common_tops["hm_chest_range_cm"]
) * 100

'''
print(
    common_tops[
        [
            "size",
            "chest_overlap_cm",
            "hm_chest_range_cm",
            "chest_overlap_percent"
        ]
    ]
)
'''


#this plots the chest measurements for H&M and Levi's
import matplotlib.pyplot as plt

'''
plt.bar(
    common_tops["size"],
    common_tops["chest_overlap_percent"]
)

plt.xlabel("Size")
plt.ylabel("Chest Range Overlap (%)")
plt.title("H&M vs Levi's Chest Range Overlap")

plt.show()
'''


'''
plt.plot(
    common_tops["size"],
    common_tops["chest_mid_cm_hm"],
    marker="o",
    label="H&M"
)

plt.plot(
    common_tops["size"],
    common_tops["chest_mid_cm_levis"],
    marker="o",
    label="Levi's"
)

plt.xlabel("Size")
plt.ylabel("Chest Midpoint (cm)")
plt.title("H&M vs Levi's Chest Measurement Comparison")

plt.legend()
plt.show()
'''




#this calculates the midpoint between min and max waist measurements for H&M and Levi's
hm_tops["waist_mid_cm"] = calculate_midpoint(
    hm_tops,
    "waist_min_cm",
    "waist_max_cm"
)

levis_tops["waist_mid_cm"] = calculate_midpoint(
    levis_tops,
    "waist_min_cm",
    "waist_max_cm"
)

'''
print(hm_tops[["size", "waist_mid_cm"]])
print(levis_tops[["size", "waist_mid_cm"]])
'''

common_tops = pd.merge(
    hm_tops,
    levis_tops,
    on="size",
    suffixes=("_hm", "_levis")
)

#this calculates the difference in waist middle point measurements between H&M and Levi's
common_tops["waist_mid_difference_cm"] = (
    common_tops["waist_mid_cm_levis"]
    - common_tops["waist_mid_cm_hm"]
)

'''
print(
    common_tops[
        ["size", "waist_mid_cm_hm",
         "waist_mid_cm_levis",
         "waist_mid_difference_cm"]
    ]
)
'''

''''
plt.plot(
    common_tops["size"],
    common_tops["waist_mid_cm_hm"],
    marker="o",
    label="H&M"
)

plt.plot(
    common_tops["size"],
    common_tops["waist_mid_cm_levis"],
    marker="o",
    label="Levi's"
)

plt.xlabel("Size")
plt.ylabel("Waist Midpoint (cm)")
plt.title("H&M vs Levi's Waist Measurement Comparison")

plt.legend()
plt.show()
'''

#find the overlapping range
common_tops["waist_overlap_min"] = common_tops[
    ["waist_min_cm_hm", "waist_min_cm_levis"]
].max(axis=1)

common_tops["waist_overlap_max"] = common_tops[
    ["waist_max_cm_hm", "waist_max_cm_levis"]
].min(axis=1)

#calculate the overlap width
common_tops["waist_overlap_cm"] = (
    common_tops["waist_overlap_max"]
    - common_tops["waist_overlap_min"]
)

common_tops.loc[
    common_tops["waist_overlap_cm"] < 0,
    "waist_overlap_cm"
] = 0

#calculate h&m waist range width
common_tops["hm_waist_range_cm"] = (
    common_tops["waist_max_cm_hm"]
    - common_tops["waist_min_cm_hm"]
)

common_tops["waist_overlap_percent"] = (
    common_tops["waist_overlap_cm"]
    / common_tops["hm_waist_range_cm"]
) * 100


'''
print(
    common_tops[
        [
            "size",
            "waist_min_cm_hm",
            "waist_max_cm_hm",
            "waist_min_cm_levis",
            "waist_max_cm_levis",
            "waist_overlap_cm",
            "waist_overlap_percent"
        ]
    ]
)
'''


'''
plt.bar(
    common_tops["size"],
    common_tops["waist_overlap_percent"]
)

plt.xlabel("Size")
plt.ylabel("Waist Range Overlap (%)")
plt.title("H&M vs Levi's Waist Range Overlap")

plt.show()
'''


#bottoms waist midpoint
#first calculate the waist midpoint for both
hm_bottoms["waist_mid_cm"] = calculate_midpoint(
    hm_bottoms,
    "waist_min_cm",
    "waist_max_cm"
)

levis_bottoms["waist_mid_cm"] = calculate_midpoint(
    levis_bottoms,
    "waist_min_cm",
    "waist_max_cm"
)

'''
print(hm_bottoms[["size", "waist_mid_cm"]])
print(levis_bottoms[["size", "waist_mid_cm"]])
'''

#we will create a common_bottoms DataFrame containing only the sizes both brands publish
#common sizes for bottoms
common_bottoms = pd.merge(
    hm_bottoms,
    levis_bottoms,
    on="size",
    suffixes=("_hm", "_levis")
)

'''
print(
    common_bottoms[
        ["size", "waist_mid_cm_hm", "waist_mid_cm_levis"]
    ]
)
'''

#calculate the midpoint difference
common_bottoms["waist_mid_difference_cm"] = (
    common_bottoms["waist_mid_cm_levis"]
    - common_bottoms["waist_mid_cm_hm"]
)

'''
print(
    common_bottoms[
        [
            "size",
            "waist_mid_cm_hm",
            "waist_mid_cm_levis",
            "waist_mid_difference_cm"
        ]
    ]
)
'''

#actual waist-range overlap
common_bottoms["waist_overlap_min"] = common_bottoms[
    ["waist_min_cm_hm", "waist_min_cm_levis"]
].max(axis=1)

common_bottoms["waist_overlap_max"] = common_bottoms[
    ["waist_max_cm_hm", "waist_max_cm_levis"]
].min(axis=1)

common_bottoms["waist_overlap_cm"] = (
    common_bottoms["waist_overlap_max"]
    - common_bottoms["waist_overlap_min"]
)

common_bottoms.loc[
    common_bottoms["waist_overlap_cm"] < 0,
    "waist_overlap_cm"
] = 0

common_bottoms["hm_waist_range_cm"] = (
    common_bottoms["waist_max_cm_hm"]
    - common_bottoms["waist_min_cm_hm"]
)

common_bottoms["waist_overlap_percent"] = (
    common_bottoms["waist_overlap_cm"]
    / common_bottoms["hm_waist_range_cm"]
) * 100

'''
print(
    common_bottoms[
        [
            "size",
            "waist_overlap_cm",
            "waist_overlap_percent"
        ]
    ]
)
'''


'''
plt.bar(
    common_bottoms["size"].astype(str),
    common_bottoms["waist_overlap_percent"]
)

plt.xlabel("Size")
plt.ylabel("Waist Range Overlap (%)")
plt.title("H&M vs Levi's Bottoms Waist Range Overlap")

plt.show()
'''


#calculate the midpoint
hm_bottoms["hip_mid_cm"] = calculate_midpoint(
    hm_bottoms,
    "hip_min_cm",
    "hip_max_cm"
)

levis_bottoms["seat_mid_cm"] = calculate_midpoint(
    levis_bottoms,
    "seat_min_cm",
    "seat_max_cm"
)

common_bottoms = pd.merge(
    hm_bottoms,
    levis_bottoms,
    on="size",
    suffixes=("_hm", "_levis")
)

'''
print(
    common_bottoms[
        ["size", "hip_mid_cm", "seat_mid_cm"]
    ]
)
'''

#Calculate the midpoint difference
common_bottoms["hip_seat_mid_difference_cm"] = (
    common_bottoms["seat_mid_cm"]
    - common_bottoms["hip_mid_cm"]
)

'''
print(
    common_bottoms[
        [
            "size",
            "hip_mid_cm",
            "seat_mid_cm",
            "hip_seat_mid_difference_cm"
        ]
    ]
)
'''

#calculate the actual overlap
common_bottoms["hip_seat_overlap_min"] = common_bottoms[
    ["hip_min_cm", "seat_min_cm"]
].max(axis=1)

common_bottoms["hip_seat_overlap_max"] = common_bottoms[
    ["hip_max_cm", "seat_max_cm"]
].min(axis=1)

common_bottoms["hip_seat_overlap_cm"] = (
    common_bottoms["hip_seat_overlap_max"]
    - common_bottoms["hip_seat_overlap_min"]
)

common_bottoms.loc[
    common_bottoms["hip_seat_overlap_cm"] < 0,
    "hip_seat_overlap_cm"
] = 0

common_bottoms["hm_hip_range_cm"] = (
    common_bottoms["hip_max_cm"]
    - common_bottoms["hip_min_cm"]
)

common_bottoms["hip_seat_overlap_percent"] = (
    common_bottoms["hip_seat_overlap_cm"]
    / common_bottoms["hm_hip_range_cm"]
) * 100

'''
print(
    common_bottoms[
        [
            "size",
            "hip_seat_overlap_cm",
            "hip_seat_overlap_percent"
        ]
    ]
)
'''


'''
plt.bar(
    common_bottoms["size"].astype(str),
    common_bottoms["hip_seat_overlap_percent"]
)

plt.xlabel("Size")
plt.ylabel("Hip/Seat Range Overlap (%)")
plt.title("H&M vs Levi's Bottoms Hip/Seat Range Overlap")

plt.show()
'''


#size finder
def find_sizes(df, measurement, min_column, max_column):
    matching_sizes = df[
        (df[min_column] <= measurement) &
        (df[max_column] >= measurement)
    ]

    return matching_sizes


'''
chest_measurement = 95

hm_matching_sizes = find_sizes(
    hm_tops,
    chest_measurement,
    "chest_min_cm",
    "chest_max_cm"
)

levis_matching_sizes = find_sizes(
    levis_tops,
    chest_measurement,
    "chest_min_cm",
    "chest_max_cm"
)
'''


'''
print("H&M matching sizes:")
print(
    hm_matching_sizes[
        ["size", "chest_min_cm", "chest_max_cm"]
    ]
)

print("\nLevi's matching sizes:")
print(
    levis_matching_sizes[
        ["size", "chest_min_cm", "chest_max_cm"]
    ]
)
'''


#find closest size
def find_closest_size(df, measurement, min_column, max_column):
    df = df.copy()

    df["distance"] = 0.0

    below_range = measurement < df[min_column]
    above_range = measurement > df[max_column]

    df.loc[below_range, "distance"] = (
        df.loc[below_range, min_column] - measurement
    )

    df.loc[above_range, "distance"] = (
        measurement - df.loc[above_range, max_column]
    )

    closest = df.loc[df["distance"].idxmin()]

    return closest


'''
closest_levis = find_closest_size(
    levis_tops,
    chest_measurement,
    "chest_min_cm",
    "chest_max_cm"
)

print("\nClosest Levi's size:")
print(
    closest_levis[
        ["size", "chest_min_cm", "chest_max_cm", "distance"]
    ]
)
'''

#this works as bothsize finder and closest size finder
def recommend_size(df, measurement, min_column, max_column):

    matching_sizes = find_sizes(
        df,
        measurement,
        min_column,
        max_column
    )

    if not matching_sizes.empty:
        return {
            "status": "exact", 
            "size": matching_sizes.iloc[0]["size"],
            "min_cm": float(matching_sizes.iloc[0][min_column]),
            "max_cm": float(matching_sizes.iloc[0][max_column])
        }

    else:
        closest = find_closest_size(
            df,
            measurement,
            min_column,
            max_column
        )

        return {
            "status": "closest",
            "size": closest["size"],
            "min_cm": float(closest[min_column]),
            "max_cm": float(closest[max_column]),
            "distance_cm": round(float(closest["distance"]), 2)
        }



'''
result1 = recommend_size(
    levis_tops,
    95,
    "chest_min_cm",
    "chest_max_cm"
)

result2 = recommend_size(
    hm_tops,
    95,
    "chest_min_cm",
    "chest_max_cm"
)

print(result1)
print(result2)
'''


#this function handle both H&M and Levi's together
def compare_brands(measurement):

    hm_result = recommend_size(
        hm_tops,
        measurement,
        "chest_min_cm",
        "chest_max_cm"
    )

    levis_result = recommend_size(
        levis_tops,
        measurement,
        "chest_min_cm",
        "chest_max_cm"
    )

    print("\nH&M")
    print("----")

    if hm_result["status"] == "exact":
        print("Exact match:", hm_result["size"])
        print(
            "Range:",
            hm_result["min_cm"],
            "-",
            hm_result["max_cm"],
            "cm"
        )
    else:
        print("No exact match")
        print("Closest size:", hm_result["size"])
        print(
            "Range:",
            hm_result["min_cm"],
            "-",
            hm_result["max_cm"],
            "cm"
        )
        print("Distance:", hm_result["distance_cm"], "cm")


    print("\nLevi's")
    print("------")

    if levis_result["status"] == "exact":
        print("Exact match:", levis_result["size"])
        print(
            "Range:",
            levis_result["min_cm"],
            "-",
            levis_result["max_cm"],
            "cm"
        )
    else:
        print("No exact match")
        print("Closest size:", levis_result["size"])
        print(
            "Range:",
            levis_result["min_cm"],
            "-",
            levis_result["max_cm"],
            "cm"
        )
        print("Distance:", levis_result["distance_cm"], "cm")



'''
chest_measurement = float(
    input("Enter your chest measurement in cm: ")
)

compare_brands(chest_measurement)
'''
