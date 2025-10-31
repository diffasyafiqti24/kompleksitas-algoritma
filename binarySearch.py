def binary_search(arr, target, low, high):
    # --- DIVIDE ---
    if low > high:
        return -1  # elemen tidak ditemukan

    mid = (low + high) // 2
    # --- CONQUER ---
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        # cari di bagian kiri
        return binary_search(arr, target, low, mid - 1)
    else:
        # cari di bagian kanan
        return binary_search(arr, target, mid + 1, high)

# --- Pengujian ---
data = [3, 9, 10, 27, 38, 43, 82]
target = 43
result = binary_search(data, target, 0, len(data) - 1)

if result != -1:
    print(f"Elemen {target} ditemukan pada indeks ke-{result}")
else:
    print(f"Elemen {target} tidak ditemukan")
