Mock Security Assessment - Inlane Freight
------------------------------------------------------------------------

## Overview
This project is a mock external security assessment performed against the Inlane Freight environment. The goal was to evaluate the organization’s security posture, identify exploitable weaknesses, and document findings in a professional penetration testing report.

The assessment followed guidance from NIST SP 800-115 and the OWASP Testing Guide. Testing included reconnaissance, scanning, exploitation, privilege escalation, and reporting.

## Key Findings
The assessment identified several high-impact weaknesses, including:

- Insecure WordPress configuration leading to remote code execution
- Stored cross-site scripting resulting in session hijacking
- OS command injection allowing remote code execution
- Windows privilege escalation to SYSTEM
- Excessive privileges and insufficient system hardening
- Limited monitoring and preventative controls


## Skills Demonstrated
- Penetration Testing
- Vulnerability Assessment
- Web Application Security
- Privilege Escalation
- Risk Analysis
- Remediation Planning
- Technical Documentation
- OWASP Testing Methodology
- NIST SP 800-115
- NIST SP 800-53 Control Mapping

## Examples of Findings
Findings were documented with severity ratings, proof-of-concept evidence, impact, affected systems, references, and remediation guidance.

Examples included:

- Remote code execution through the WordPress Theme Editor
- Stored XSS and session hijacking
- Command injection in a monitoring application
- Windows token impersonation and privilege escalation

:contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6} :contentReference[oaicite:7]{index=7}

## Remediation
The project also focused on translating technical findings into actionable recommendations, including:

- Enforcing least privilege
- Improving input validation and output encoding
- Applying stronger application hardening
- Restricting unnecessary services
- Improving egress filtering and monitoring
- Using low-privilege service accounts

## Report
[View the Full Security Assessment Report](./JosephPatnoe_PenTestReport_Final.pdf)
