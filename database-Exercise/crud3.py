import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("market.db")
cursor = conn.cursor()

# Función para verificar si un usuario existe por número de identificación o email
def usuario_existe(identificacion, email):
    cursor.execute("SELECT * FROM users WHERE ide_number = ? OR email = ?", (identificacion, email))
    return cursor.fetchone() is not None

# Opción 1: Crear nuevo usuario
def crear_usuario():
    id_num = input("Ingrese número de identificación: ")
    email = input("Ingrese email: ")

    if usuario_existe(id_num, email):
        print("❌ Usuario con ese ID o Email ya existe.")
        return

    nombre = input("Ingrese nombre: ")
    activo = input("¿Usuario activo? (S/N): ").strip().upper() == "S"

    cursor.execute("""
        INSERT INTO users (firstname, lastname, ide_number, email, status, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, datetime('now'), datetime('now'))
    """, (nombre, "", id_num, email, int(activo)))
    conn.commit()
    print("✅ Usuario creado exitosamente.")

# Opción 2: Listar todos los usuarios
def listar_todos():
    cursor.execute("SELECT ide_number, firstname, email, status FROM users")
    usuarios = cursor.fetchall()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    print("{:<10} {:<20} {:<25} {:<10}".format("ID", "Nombre", "Email", "Activo"))
    print("-"*65)
    for u in usuarios:
        print("{:<10} {:<20} {:<25} {:<10}".format(u[0], u[1], u[2], str(bool(u[3]))))

# Opción 3: Listar usuarios activos
def listar_activos():
    cursor.execute("SELECT ide_number, firstname, email FROM users WHERE status = 1")
    activos = cursor.fetchall()
    if not activos:
        print("No hay usuarios activos.")
        return
    print("{:<10} {:<20} {:<25} {:<10}".format("ID", "Nombre", "Email", "Activo"))
    print("-"*65)
    for u in activos:
        print("{:<10} {:<20} {:<25} {:<10}".format(u[0], u[1], u[2], "True"))

# Opción 4: Listar usuarios inactivos
def listar_inactivos():
    cursor.execute("SELECT ide_number, firstname, email FROM users WHERE status = 0")
    inactivos = cursor.fetchall()
    if not inactivos:
        print("No hay usuarios inactivos.")
        return
    print("{:<10} {:<20} {:<25} {:<10}".format("ID", "Nombre", "Email", "Activo"))
    print("-"*65)
    for u in inactivos:
        print("{:<10} {:<20} {:<25} {:<10}".format(u[0], u[1], u[2], "False"))

# Opción 5: Actualizar usuario
def actualizar_usuario():
    id_num = input("Ingrese el ID del usuario a actualizar: ")
    cursor.execute("SELECT firstname, email FROM users WHERE ide_number = ?", (id_num,))
    usuario = cursor.fetchone()
    if not usuario:
        print("❌ Usuario no encontrado.")
        return

    nuevo_nombre = input(f"Nuevo nombre ({usuario[0]}): ") or usuario[0]
    nuevo_email = input(f"Nuevo email ({usuario[1]}): ") or usuario[1]
    activo = input("¿Usuario activo? (S/N): ").strip().upper() == "S"

    cursor.execute("""
        UPDATE users SET firstname = ?, email = ?, status = ?, updated_at = datetime('now')
        WHERE ide_number = ?
    """, (nuevo_nombre, nuevo_email, int(activo), id_num))
    conn.commit()
    print("✅ Usuario actualizado.")

# Opción 6: Eliminar usuario
def eliminar_usuario():
    id_num = input("Ingrese el ID del usuario a eliminar: ")
    cursor.execute("DELETE FROM users WHERE ide_number = ?", (id_num,))
    if cursor.rowcount == 0:
        print("❌ Usuario no encontrado.")
    else:
        conn.commit()
        print("✅ Usuario eliminado.")

# Opción 7: Buscar usuario
def buscar_usuario():
    criterio = input("Ingrese nombre o email a buscar: ").lower()
    cursor.execute("""
        SELECT ide_number, firstname, email, status FROM users
        WHERE LOWER(firstname) LIKE ? OR LOWER(email) LIKE ?
    """, (f"%{criterio}%", f"%{criterio}%"))
    encontrados = cursor.fetchall()
    if not encontrados:
        print("No se encontraron usuarios.")
        return
    print("{:<10} {:<20} {:<25} {:<10}".format("ID", "Nombre", "Email", "Activo"))
    print("-"*65)
    for u in encontrados:
        print("{:<10} {:<20} {:<25} {:<10}".format(u[0], u[1], u[2], str(bool(u[3]))))

# Menú principal
def menu():
    while True:
        print("\n--- Main Menu ---")
        print("[1] Create new user")
        print("[2] List all users")
        print("[3] List active users")
        print("[4] List inactive users")
        print("[5] Update user")
        print("[6] Delete user")
        print("[7] Search user")
        print("[8] Exit")

        opcion = input("Press any option: ")

        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 8:
            print("❌ Opción inválida. Intente nuevamente.")
            continue

        opcion = int(opcion)

        if opcion == 1:
            crear_usuario()
        elif opcion == 2:
            listar_todos()
        elif opcion == 3:
            listar_activos()
        elif opcion == 4:
            listar_inactivos()
        elif opcion == 5:
            actualizar_usuario()
        elif opcion == 6:
            eliminar_usuario()
        elif opcion == 7:
            buscar_usuario()
        elif opcion == 8:
            print("👋 Saliendo del programa...")
            break

# Ejecutar menú
menu()

# Cerrar conexión
conn.close()