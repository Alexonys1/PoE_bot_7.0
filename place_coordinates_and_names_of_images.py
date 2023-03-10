from point_coordinates import Point, Region


# Координаты разных точек программы
coordinates_of_stash = Point (676, 420)
coordinates_of_currency_tab_in_inventory = Point (140, 120)
coordinates_of_sextant_in_currency_tab = Point (385, 370)
coordinates_of_compass_in_currency_tab = Point (140, 560)
coordinates_of_craft_place = Point (655, 845)
coordinates_of_guild_stash = Point (590, 410)
coordinates_of_big_guild_tab_in_guild_stash = Point (375, 120)
coordinates_of_place_near_craft_place_where_there_is_nothing = Point (735, 890)

# Регионы
stash_region = Region (7, 130, 570, 570)
sextant_region_in_inventory = Region (695, 540, 105, 240)
compass_region_in_inventory = Region (790, 540, 55, 240)
region_of_charged_compasses_in_inventory = Region (835, 540, 430, 240)

# Пути к фото
image_name_of_empty_inventory_cell = r"..\images\The empty inventory cell.PNG"
name_of_image_with_selected_sextant_in_currency_tab = r"..\images\The selected sextant in the currency tab.PNG"
name_of_image_with_selected_compass_in_currency_tab = r"..\images\The selected compass in the currency tab.PNG"
name_of_image_with_unselected_sextant_in_inventory = r"..\images\The unselected sextant in the inventory.PNG"
name_of_image_with_unselected_compass_in_inventory = r"..\images\The unselected compass in the inventory.PNG"
name_of_image_with_unselected_charged_compass_in_inventory = r"..\images\The unselected charged compass in the inventory.PNG"