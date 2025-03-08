from obj_reader import ObjReader

def main():
    obj = ObjReader('inputs/icosahedron.obj')
    obj.print_faces()

if __name__ == "__main__":
    main()
