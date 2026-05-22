``` d2
Main: {
    App: {
        shape: class
        __init__()
        setup_cli_parser()
        setup_parser_optionals()

        }
    cli opts: |md 
    - c config
    - u update 
    - r regex
    - m mediaupdate
    - R recursive
    |
        
}
Config: {
    shape: class
    __init__()
    setup_syntax()
    setup_defaults()
    update_config()
    load_syntax()
    }

AnkiConnect: {
    shape: class
    request()
    invoke(): parseOut
    parse(): 
    }

Note: {
    shape: ID_REGEXP
    __init__()
    field_from_line()
    fields()

    }
RegexNote: {
    shape: class
    __init__()
    fields()

    }



```


App manages everything

Config saves and looads Config file

Data is the json file holding the hashed/unhashed stuff


