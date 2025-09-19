from controllers.product_controller import ProductController

class ProductView:
    def __init__(self):
        self.ctrl = ProductController()

    def show_menu(self):
        while True:
            print("\n=== Produits ===")
            print("1. Montrer la liste d'items")
            print("2. Ajouter un item")
            print("3. Supprimer un item")
            print("4. Retour")
            choice = input("Choix: ").strip()

            if choice == "1":
                self.show_list()
            elif choice == "2":
                self.add_item()
            elif choice == "3":
                self.delete_item()
            elif choice == "4":
                break
            else:
                print("Option invalide.")

    def show_list(self):
        products = self.ctrl.list_products()
        if not products:
            print("(Aucun produit)")
        for p in products:
            print(f"{p.id}: {p.name} [{p.brand}] - {p.price:.2f}$")

    def add_item(self):
        name = input("Nom: ").strip()
        brand = input("Marque: ").strip()
        price = float(input("Prix: ").strip())
        new_id = self.ctrl.add_product(name, brand, price)
        print(f"Ajouté avec id {new_id}")

    def delete_item(self):
        pid = int(input("Id à supprimer: ").strip())
        self.ctrl.delete_product(pid)
        print("Supprimé.")