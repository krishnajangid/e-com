from fastapi_sqlalchemy import db

from models.category import CategoryModel


class CategoryMod:

    def __init__(self):
        pass

    def get_all_category(self, page, per_page):
        category_obj = db.session.query(CategoryModel).filter(
            CategoryModel.active == True,
            CategoryModel.parent_id == None
        )
        total_result = category_obj.count()
        category_obj_list = category_obj.offset((page * per_page) - per_page).limit(per_page).all()
        result_dict = {
            "page_number": page,
            "page_size": per_page,
            "total": total_result,
            "result": self.__get_category(category_obj_list)
        }

        return result_dict

    def __get_category(self, category_obj_list):
        category_dict_list = []
        for category_obj in category_obj_list:
            child_category_obj = db.session.query(CategoryModel).filter(
                CategoryModel.parent_id == category_obj.id).all()
            category_dict_list.append({
                "id": category_obj.id,
                "name": category_obj.name,
                "description": category_obj.description,
                "sort_order": category_obj.sort_order,
                "child": self.__get_category(child_category_obj)
            })
        return category_dict_list