from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, Item, User

engine = create_engine('postgres://itoebvbeobxksl:d75445491f0f66b9b2360a19094658ad1119509b52c3e82144f6fb179228f3b8@ec2-54-221-237-246.compute-1.amazonaws.com:5432/d43ksk0d1rnbdj')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create test User
User1 = User(name="Test User",
             email="testUser@outdoor.com",
             picture=(
                'https://pbs.twimg.com/profile_images/2671170543/' +
                '18debd694829ed78203a5a36dd364160_400x400.png'))
session.add(User1)
session.commit()

# Create Categories
category1 = Category(name="Camping")
session.add(category1)
session.commit()

category2 = Category(name="Hiking")
session.add(category2)
session.commit()

category3 = Category(name="Boating")
session.add(category3)
session.commit()

category4 = Category(name="Fishing")
session.add(category4)
session.commit()

category5 = Category(name="Hunting")
session.add(category5)
session.commit()

# Add Items
item1 = Item(name="Tent",
             description=(
                "Brand new tent that fits up to 6 people! " +
                "Includes two seperate rooms and doorways " +
                "as well as several windows"),
             image=(
                "https://images.snowys.com.au/content/images/" +
                "thumbs/0000906_traveller-3p-tent_1100.jpeg"),
             category=category1,
             user=User1)
session.add(item1)
session.commit()

item2 = Item(name="Stove",
             description=(
                "Slightly used stove with two burners. Can " +
                "use small or large propane bottles and " +
                "cooks well!"),
             image=(
                "https://www.rei.com/media/product/115536"),
             category=category1,
             user=User1)
session.add(item2)
session.commit()


item3 = Item(name="Boots",
             description=(
                "Brand new hiking boots! Lots of padding for " +
                "comfort, excellent tread for traction,  and strong outer" +
                " lining for added protection!"),
             image=(
                "https://www.rei.com/media/1b1b50f6-9987-4a33-b12c-" +
                "8eb83dc94c04?size=1020x510"),
             category=category2,
             user=User1)
session.add(item3)
session.commit()

item4 = Item(name="Life Jacket",
             description=(
                "Life safety vest that will keep your family " +
                "safe while out on the boat! This vest comes in an " +
                "assortment of colors"),
             image=(
                "https://i5.walmartimages.com/asr/7d3e5a31-0d06" +
                "-4e7e-9996-a245b3cb27d7_1.28ec5407c57ffedbb8ed" +
                "a448ec987d95.jpeg?odnHeight=450&odnWidth=450&" +
                "odnBg=FFFFFF"),
             category=category3,
             user=User1)
session.add(item4)
session.commit()

item5 = Item(name="Fishing Pole",
             description=(
                "Fiberglass fishing pole specially designed " +
                "for those large fish you will surely catch! "),
             image=(
                "https://s7d2.scene7.com/is/image/dkscdn/15SKSUSGX2" +
                "SPN7F1PROD_is"),
             category=category4,
             user=User1)
session.add(item5)
session.commit()

item6 = Item(name="Safety Vest",
             description=(
                "Bright orange safety vest to provide " +
                "protection to you and your hunting partners!"),
             image=(
                "https://s7d2.scene7.com/is/image/dkscdn/15GHDUFR" +
                "NTLDRVSTBAOT_is/?$searchGrid$&wid=180&hei=180"),
             category=category5,
             user=User1)
session.add(item6)
session.commit()

item7 = Item(name="Chair",
             description=(
                 "Basic camping chair for sitting around the campfire." +
                 " This chair comes in a wide array of colors and " +
                 "additional features can be added on!"),
             image=(
                 "http://media.4rgos.it/i/Argos/9278321_R_Z001A_UC127" +
                 "8555?$Web$&$DefaultPDP570$"),
             category=category1,
             user=User1)
session.add(item7)
session.commit()

item8 = Item(name="Lantern",
             description=(
                "Lantern to provide light when you are out " +
                "in the dark wilderness!"),
             image=(
                "https://encrypted-tbn0.gstatic.com/images?" +
                "q=tbn:ANd9GcQ87rwM26-My3qkOjiUawVgRweq8115O" +
                "SM75dUZxrYrYaCWW2Wp"),
             category=category1,
             user=User1)
session.add(item8)
session.commit()
