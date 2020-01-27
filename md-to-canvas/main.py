import httpx
import toml
import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

headers = {"Authorization": f"Bearer {os.getenv('CANVAS_TOKEN')}"}


"""
returns {
  // the unique identifier for the module
    "id": 123,
  // the state of the module: 'active', 'deleted'
  "workflow_state": "active",
  // the position of this module in the course (1-based)
  "position": 2,
  // the name of this module
  "name": "Imaginary Numbers and You",
  // (Optional) the date this module will unlock
  "unlock_at": "2012-12-31T06:00:00-06:00",
  // Whether module items must be unlocked in order
  "require_sequential_progress": true,
  // IDs of Modules that must be completed before this one is unlocked
  "prerequisite_module_ids": [121, 122],
  // The number of items in the module
  "items_count": 10,
  // The API URL to retrive this module's items
  "items_url": "https://canvas.example.com/api/v1/modules/123/items",
  // The contents of this module, as an array of Module Items. (Present only if
  // requested via include[]=items AND the module is not deemed too large by
  // Canvas.)
  "items": null,
  // The state of this Module for the calling user one of 'locked', 'unlocked',
  // 'started', 'completed' (Optional; present only if the caller is a student or
  // if the optional parameter 'student_id' is included)
  "state": "started",
  // the date the calling user completed the module (Optional; present only if the
  // caller is a student or if the optional parameter 'student_id' is included)
  "completed_at": null,
  // if the student's final grade for the course should be published to the SIS
  // upon completion of this module
  "publish_final_grade": null,
  // (Optional) Whether this module is published. This field is present only if
  // the caller has permission to view unpublished modules.
  "published": true
}
"""


def create_module(name):
    url = f"{os.getenv('CANVAS_API_URL')}/api/v1/courses/{os.getenv('CANVAS_COURSE_ID')}/modules"
    module = {"module[name]": name}

    r = httpx.post(url, headers=headers, params=module)
    return r.json()


def delete_module(module_id):
    url = f"{os.getenv('CANVAS_API_URL')}/api/v1/courses/{os.getenv('CANVAS_COURSE_ID')}/modules/{module_id}"

    r = httpx.delete(url, headers=headers)
    return r.json()


def create_module_subheader(module_id, title):
    url = f"{os.getenv('CANVAS_API_URL')}/api/v1/courses/{os.getenv('CANVAS_COURSE_ID')}/modules/{module_id}/items"
    module_item = {"module_item[title]": title, "module_item[type]": "SubHeader"}

    r = httpx.post(url, headers=headers, params=module_item)
    return r.json()


def create_module_page(module_id, subheader_id, title, body):
    page_url = title.lower().replace(" ", "-")
    url = f"{os.getenv('CANVAS_API_URL')}/api/v1/courses/{os.getenv('CANVAS_COURSE_ID')}/pages/{page_url}"
    module_page = {"wiki_page[title]": title, "wiki_page[body]": body}

    page_creation = httpx.put(url, headers=headers, params=module_page)
    page_id = page_creation.json()["page_id"]
    page_url = page_creation.json()["url"]

    url = f"{os.getenv('CANVAS_API_URL')}/api/v1/courses/{os.getenv('CANVAS_COURSE_ID')}/modules/{module_id}/items"
    module_item = {
        "module_item[title]": title,
        "module_item[type]": "Page",
        "module_item[content_id]": subheader_id,
        "module_item[page_url]": page_url,
    }
    page_connection = httpx.postv(url, headers=headers, params=module_item)
    return page_connection.json()


res = create_module_page(780, 10364, "Test Page Title", "Test page body!")


print(res)

# async def create_module_item(course_id, module_id, title):
#     url = f"/api/v1/courses/${course_id}/modules/${module_id}/items"
#     module_item = {course_id, module_id, title}

#     async with httpx.AsyncClient() as client:
#         r = await client.post(url, params=params)
