# Diamond or RageQuit

```
+-----------------+     +--------+     +----------+
| SC2 replay file | --> | Parser | --> | database |
+-----------------+     +--------+     +----------+


+----------+     +-----------+     +----------------------------+
| database | --> | webserver | --> | Sortable interactive table |
+----------+     +-----------+     +----------------------------+
```

# Table Fields

Date | map | matchup | opponent:name | opp:race | opp:League | user:race | user:League | time | result |  Creep spread % | Workers Created | MaxTime | avg unspent resources | time supply capped




# SC2 Reader (parser)
* https://github.com/GraylinKim/sc2reader
* https://sc2reader.readthedocs.io/en/latest/articles/gettingstarted.html
* https://sc2reader.readthedocs.io/en/latest/tutorials/prettyprinter.html


# Database 
* https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
* https://leportella.com/english/2019/01/10/sqlalchemy-basics-tutorial.html
* https://docs.sqlalchemy.org/en/13/dialects/sqlite.html
* https://docs.sqlalchemy.org/en/13/core/engines.html
* https://medium.com/@mahmudahsan/how-to-use-python-sqlite3-using-sqlalchemy-158f9c54eb32
* https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
* https://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/
* https://www.pythonsheets.com/notes/python-sqlalchemy.html


# Webserver (flask)
* https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/


# Sortable - interactive table (?)
**Possibly Bootstrap Related?**
* should be able to reorder columns on the fly




# Stretch Goals
Interesting Statistics
- Matchup W/L ratios
- Charts / graphs


