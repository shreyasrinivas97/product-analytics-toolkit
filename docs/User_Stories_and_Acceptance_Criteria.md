# Backlog: User Stories and Acceptance Criteria

## Epic 1 — Guided onboarding
### US-01: View onboarding checklist
**As a** new user, **I want** a short checklist, **so that** I know the next useful action.
- Given an eligible user with an incomplete setup, when the home screen loads, then the checklist is visible.
- Each step has a label, action, and status.
- Checklist is keyboard accessible and works at supported viewport sizes.

### US-02: Complete or dismiss checklist
**As a** user, **I want** to mark steps complete or dismiss the checklist, **so that** it does not keep interrupting me.
- Completion updates the step status and progress indicator.
- Dismissal hides the checklist and persists the preference.
- Reopening the app does not reset persisted completion state.

## Epic 2 — Search refinement
### US-03: Apply search filters
**As a** returning user, **I want** to apply filters, **so that** I can narrow results.
- User can apply supported filters individually and in combination.
- Active filters are visibly represented.
- Results update and loading/error states are clear.

### US-04: Clear filters and recover from no results
**As a** user, **I want** to clear filters, **so that** I can recover when no results match.
- “Clear all” resets every active filter.
- Empty state explains that no results matched and offers a recovery action.
- Filter state and result count remain consistent.

## Epic 3 — Measurement
### US-05: Track product events
**As a** product team, **I want** consistent event tracking, **so that** adoption and outcomes can be measured.
- Events: onboarding_viewed, onboarding_step_completed, onboarding_dismissed, filter_applied, filters_cleared, search_result_clicked.
- Events include a pseudonymous user/session key, timestamp, platform, and experiment variant where applicable.
- Events do not include raw personal information.
- QA verifies events in a staging/debug view before launch.

## Suggested backlog prioritization
1. Event instrumentation and baseline validation (dependency).
2. Guided onboarding MVP.
3. Search filter MVP after validating filter demand and technical feasibility.
4. Follow-up improvements based on observed usage and user research.
