# Minetest Media collection

Remote Media collection for Minetest

Uses Automatic collection of media files and links

Tags for link collections are:
- core
- mtgame
- mtmods
- contentdb

Skins are fetched using the extra update_skins.py script

[contentdb](https://content.minetest.net/) and [skins](http://minetest.fensta.bplaced.net/) are automaticly fetched from the databases

The lower ones always also contain the higher ones.

## Remote Media Links

Only the first one works right now! The others need a [change](https://github.com/Lejo1/minetest/commit/69b6319dfdabb267f15d59bdd591741ed471998f)

- http://lejo1.gitlab.io/mtmedia/
- https://lejo1.github.io/mtmedia/m/
- https://raw.githubusercontent.com/Lejo1/mtmedia/master/m/
- https://cdn.jsdelivr.net/gh/Lejo1/mtmedia/m/
- https://ghcdn.rawgit.org/Lejo1/mtmedia/master/m/
- https://rawcdn.githack.com/Lejo1/mtmedia/6924d63f4cc9685d290fb05c96fb6e7c8b40f484/m/

## Setup

The good thing is you can use multiple remote servers. This setup is fully backward compatible and also works for older clients.

minetest.conf:  
`remote_media = https://cdn.jsdelivr.net/gh/Lejo1/mtmedia/m/,http://lejo1.gitlab.io/mtmedia/`
