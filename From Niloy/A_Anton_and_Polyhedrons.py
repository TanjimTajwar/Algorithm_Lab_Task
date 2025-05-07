face_count = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

n = int(input())
total_faces = 0

for _ in range(n):
    polyhedron = input().strip()
    total_faces += face_count[polyhedron]

print(total_faces)
