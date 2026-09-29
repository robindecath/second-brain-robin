# Media Alternatives

## Overview

Accessible alternatives cover two categories:

**Images (WCAG 1.1.1)**: every non-text image needs an `alt` attribute describing its purpose. Decorative images use `alt=""` so assistive technology ignores them. Informative images describe meaning in the alt text. Functional images (buttons, links) describe the action, not the appearance. Complex images (charts, diagrams) add an extended description. Empty or missing alt text on informative images is a critical violation.

**Time-based media / audio-video (WCAG 1.2.x)**: audio and video must provide text or synchronized alternatives for users who are deaf, hard of hearing, blind, or deafblind. WCAG 1.2.x covers five types of media alternatives. (WCAG 1.2.1–1.2.5 AA)

## Types of Media and Required Alternatives

| Media type | Required alternative (AA) | WCAG |
|---|---|---|
| Audio-only (pre-recorded) | **Transcript** | 1.2.1 |
| Video-only (pre-recorded, no audio) | **Text description** or **audio description track** | 1.2.1 |
| Video + audio (pre-recorded) | **Captions** (synchronized) | 1.2.2 |
| Video + audio (pre-recorded) | **Audio description** (or full text transcript) | 1.2.5 |
| Video + audio (live) | **Live captions** | 1.2.4 |

> **AAA extras**: Sign language interpretation (1.2.6), extended audio description (1.2.7), media alternative for all pre-recorded (1.2.8), audio-only live (1.2.9).

## Captions vs. Subtitles

**Captions** include all spoken dialogue **plus** non-speech audio (sound effects, music, speaker identification). They serve deaf and hard-of-hearing users.

**Subtitles** are translations of spoken content only. They do not replace captions for accessibility.

## Audio Descriptions

Audio descriptions narrate visual information not conveyed in dialogue (scene descriptions, on-screen text, actions). They are inserted during natural pauses in the audio track.

When the video does not have sufficient pauses, **extended audio descriptions** pause the video to insert longer descriptions.

## Transcript Requirements

A transcript must contain:
- All spoken dialogue
- Identification of speakers
- Non-speech audio that conveys meaning
- Descriptions of important visual content (for deaf-blind users accessing via braille display)

## Platform Implementation

- **Web**: Use `<track kind="captions">` for HTML `<video>`, or ensure embedded players (YouTube, Vimeo) have captions enabled. Provide `<a href="transcript.html">` links near the player.
- **iOS**: `AVPlayer` supports `AVMediaCharacteristicLegible` for caption tracks. `../../references/references/` for VoiceOver overlay patterns.
- **Android**: `ExoPlayer` / `MediaPlayer` support caption tracks via `SubtitleView`. Check `../../references/references/` for media patterns.

## Resources

- WCAG 1.2.1 Audio-only and Video-only: <https://www.w3.org/WAI/WCAG22/Understanding/audio-only-and-video-only-prerecorded>
- WCAG 1.2.2 Captions (Prerecorded): <https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded>
- WCAG 1.2.4 Captions (Live): <https://www.w3.org/WAI/WCAG22/Understanding/captions-live>
- WCAG 1.2.5 Audio Description: <https://www.w3.org/WAI/WCAG22/Understanding/audio-description-prerecorded>
- W3C Media Accessibility: <https://www.w3.org/WAI/media/av/>
