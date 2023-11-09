# Smart Manager Versioning Guidelines

Smart Manager follows a structured versioning system that adheres to the GitHub Semantic Versioning Tags. Our versioning format is as follows:

**[Major].[Minor].[Patch]-[Stage]**

Let's break down what each part of this version format means:

## Major Releases

Major releases signify significant changes to the application's behavior. These updates introduce substantial new features, redesign core elements, or alter the fundamental implementation of the application. It's important to note that major versions are not backward compatible, meaning data saved by a previous version cannot be imported into the latest major release.

Examples of major changes include overhauls in the Authentication Subsystem or transitioning from a command-line interface to a graphical user interface.

## Minor Releases

Minor releases bring new features and improvements to enhance the user experience without altering the core design or implementation of the application. Minor versions are backward compatible, meaning data saved by a previous version can seamlessly migrate to the latest minor release.

Minor changes, except for the data handling and encryption subsystems, don't significantly impact user experience or overall functionality.

## Patch Releases

Patch releases, also known as batch releases, focus on fixing bugs and making minimal or subtle changes that may not be immediately noticeable to the user. Similar to minor releases, patch versions are backward compatible, allowing smooth data import from previous versions.

Typical scenarios for patch releases include resolving bugs and enhancing the application's error handling. Additionally, optimizing algorithms to improve application efficiency falls under this category.

## Release Stages

Smart Manager versions may include optional flags, indicating the stage of the release. We utilize three primary flags:

### Alpha

Alpha releases are experimental versions with features under development. These releases are not suitable for production or personal use. Alpha versions serve as a testing ground for developers in real production environments, with no guarantee of application stability or data safety. Use alpha releases exclusively for code testing and development purposes.

### Beta

Beta releases contain features under development but have undergone testing by developers. Beta versions are more stable than alpha releases and provide a safer environment for user feedback. While beta versions may still have some features in development, they are suitable for testing by a broader audience.

### Stable

Stable releases are fully developed versions that provide a robust user experience. The code of stable releases has undergone comprehensive testing by developers. These versions are recommended for production-level usage and are considered safe for everyday tasks.

Before using any release for production or personal purposes, it is essential to be familiar with the project's license terms and conditions.

## Normal Releases

Releases without optional flags are considered normal releases. They offer a stability level between beta and stable releases. These versions aim to bridge the gap, providing dependable performance without the experimental nature of beta releases or the full stability of stable releases.
