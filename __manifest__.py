{
    "name": "Dudoxx Encounter",
    "version": "1.0",
    "author": "Walid Boudabbous, DUDOXX UG",
    "category": "Healthcare",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/dudoxx_encounter_views.xml",
        "views/main_menu.xml"
    ],
    "assets": {
        "web.assets_backend": [
            "dudoxx_encounter/static/src/css/dudoxx_encounter.css",
            "dudoxx_encounter/static/src/js/dudoxx_encounter.js"
        ]
    },
    "installable": true,
    "application": true
}
