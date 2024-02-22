from app import app
from models import db, Cupcake


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

db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10])
db.session.commit()