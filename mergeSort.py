def merge_sort(arr):
    # --- DIVIDE ---
    if len(arr) <= 1:
        return arr  # basis: array berukuran 1 sudah terurut

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # --- CONQUER ---
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # --- COMBINE ---
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """Fungsi untuk menggabungkan dua list terurutan"""
    result = []
    i = j = 0

    # Proses penggabungan dua list terurut
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Tambahkan sisa elemen
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- Pengujian ---
data = [38, 27, 43, 3, 9, 82, 10]
print("Data awal:", data)
sorted_data = merge_sort(data)
print("Setelah Merge Sort:", sorted_data)
