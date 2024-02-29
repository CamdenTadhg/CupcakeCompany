from app import app
from models import db, Cupcake, Ingredient


db.drop_all()
db.create_all()

c1 = Cupcake(flavor = 'Chocolate Chip Cookie Dough', size = 'extra small', rating=9, image='https://www.nadiacakes.com/application/files/cache/f6a3b1dbe70723808613fb91275b8cae.png')
c2 = Cupcake(flavor = 'Rosemary Lavender', size='large', rating=5, image='https://www.nadiacakes.com/application/files/cache/671388f5ada142c310e57d8f172f8483.png')
c3 = Cupcake(flavor='Pretty in Pink', size='medium', rating=6, image='https://www.nadiacakes.com/application/files/cache/baa313acde0a407dc54f8016d2cea24a.png')
c4 = Cupcake(flavor='Wedding Cake', size='large', rating=10, image='https://www.nadiacakes.com/application/files/cache/8617d955ad8320ddf2c720cc44c7c2f4.png')
c5 = Cupcake(flavor="Brownie Cupcake", size="extra small", rating=8, image='https://www.nadiacakes.com/application/files/cache/4fd0855518ac8a71d43d6cd96ea57448.png')
c6 = Cupcake(flavor="Chocolate Vanilla", size="medium", rating=5, image='https://www.nadiacakes.com/application/files/cache/21a6ea41dc105e048240ca967494f321.png')
c7 = Cupcake(flavor="Cookies & Cream", size="extra large", rating=9, image='https://www.nadiacakes.com/application/files/cache/1f780e08b5e3d5123e6f3d2110dee226.png')
c8 = Cupcake(flavor="Doggie Cupcake", size="small", rating=5, image='https://www.nadiacakes.com/application/files/cache/c821f2a15d812d46fb25caba00e7d55c.png')
c9 = Cupcake(flavor="Lemon Drop", size="small", rating=6, image='https://www.nadiacakes.com/application/files/cache/fba552e221c819585b51567f35b02a3c.png')
c10 = Cupcake(flavor="Peanut Butter Cup", size="medium", rating=7, image='https://www.nadiacakes.com/application/files/cache/79356d90906180b59e7c4e6a745c6ca1.png')
c11 = Cupcake(flavor="Orange Blossom", size="medium", rating=6, image="https://www.nadiacakes.com/application/files/cache/11f2d9689a417ae72980088602c8c605.png")
c12 = Cupcake(flavor="Orange Chicken", size="extra large", rating=5, image="https://www.nadiacakes.com/application/files/cache/05f99973038910b416244fce697f746a.png")
c13 = Cupcake(flavor="Orange Chocolate Truffle", size="large", rating=7, image="https://www.nadiacakes.com/application/files/cache/afb12da3b3fce9554b513a82e0f649c6.png")
c14 = Cupcake(flavor="Orange Dreamsicle", size="small", rating=4, image="https://www.nadiacakes.com/application/files/cache/7502d2c744a3beffc1057b5b5d628c3e.png")
c15 = Cupcake(flavor="Orange Vanilla bean Cheesecake", size="extra small", rating=8, image="https://www.nadiacakes.com/application/files/cache/0a667d7144db558d6e0668a46b26d2b2.png")
c16 = Cupcake(flavor="Orange You Glad I Said Chocolate?", size="extra small", rating=5, image="https://www.nadiacakes.com/application/files/cache/feeba7d0f23ecb5eef7fa9f1e19d0219.png")


db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16])
db.session.commit()

i1 = Ingredient(name="cream cheese frosting")
i2 = Ingredient(name="granulated sugar")
i3 = Ingredient(name="all-purpose flour")
i4 = Ingredient(name="cocoa powder")
i5 = Ingredient(name="powdered sugar")
i6 = Ingredient(name="sea salt")
i7 = Ingredient(name="eggs")
i8 = Ingredient(name="canola oil")
i9 = Ingredient(name="water")
i10 = Ingredient(name="vanilla")
i11 = Ingredient(name="marshmallow frosting")
i12 = Ingredient(name="marshmallows")
i13 = Ingredient(name="yams")
i14 = Ingredient(name="carrots")
i15 = Ingredient(name="walnuts")
i16 = Ingredient(name="cinnamon")
i17 = Ingredient(name="allspice")

db.session.add_all([i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17])
db.session.commit()