--SQLite
-- メニューテーブルの作成
CREATE TABLE menu (
    menu_id INTEGER PRIMARY KEY,
    menu_name TEXT NOT NULL,
    category_code INTEGER NOT NULL,
    cooking_time INTEGER
);

-- 食材テーブルの作成
CREATE TABLE ingredient (
    ingredient_id INTEGER PRIMARY KEY,
    ingredient_name TEXT NOT NULL,
    category_code TEXT NOT NULL,
    allergen_level INTEGER NOT NULL
);

-- メニューと食材の紐づけテーブルの作成
CREATE TABLE menu_ingredient (
    menu_id INTEGER,
    ingredient_id INTEGER,
    PRIMARY KEY (menu_id, ingredient_id),
    FOREIGN KEY (menu_id) REFERENCES menu(menu_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredient(ingredient_id)
);

-- コードと名前を管理するテーブルの作成
CREATE TABLE code_value (
    code TEXT PRIMARY KEY,
    name TEXT NOT NULL
);