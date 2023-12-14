<div align="center">

# Outlines Functions 🏭

<img src="./logo.png" alt="Outlines Logo" width=300></img>

[![Contributors][contributors-badge]][contributors]
[![Discord][discord-badge]][discord]
[![Twitter][twitter-badge]][twitter]

*Ready-to-deploy programs written with Outlines*

[Contribute new functions](https://github.com/outlines-dev/functions/pulls)  •
[Share your ideas][discord]

</div>

## How to use functions?

Oultines Functions 🏭 is a repository of programs written with [Outlines  〰️](https://github.com/outlines-dev/outlines), and that can be downloaded and executed by Outlines:

``` python
import outlines


summarizer = outlines.Function.from_github("outlines-dev/functions/src/summarization")
result = summarizer("Summarize this.")
```

## Available functions

- [Summarization](https://github.com/outlines-dev/functions/blob/main/src/summarization.py) uses chain-of-density to summarize documents. Initialize the function and pass the document you need to be summarized. Import with `outlines-dev/functions/src/summarization`

## Contribute

Outlines functions are a community effort! Have any ideas? You can open an Issue or a Pull Request on this repo. You can even store them in your own repo 😊 And come [chat with us][discord] to share your work!

## License

Outlines functions are open-source and licensed under the [Apache License 2.0](LICENSE).

[contributors]: https://github.com/outlines-dev/functions/graphs/contributors
[contributors-badge]: https://img.shields.io/github/contributors/outlines-dev/functions?style=flat-square&logo=github&logoColor=white&color=ECEFF4
[twitter]: https://twitter.com/dottxtai
[twitter-badge]: https://img.shields.io/twitter/follow/dottxtai?style=social
[discord]: https://discord.gg/R9DSu34mGd
[discord-badge]: https://img.shields.io/discord/1182316225284554793?color=81A1C1&logo=discord&logoColor=white&style=flat-square
