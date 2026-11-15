import styles from './EducationSection.module.css'

export default function EducationSection({ education }) {
  return (
    <div className={styles.section}>
      <h2 className={styles.title}>Education</h2>
      <div className={styles.cards}>
        {education.map((edu, i) => (
          <div key={i} className={styles.card}>
            <div className={styles.institution}>{edu.institution}</div>
            <div className={styles.degree}>{edu.degree}</div>
            {edu.period && <div className={styles.period}>{edu.period}</div>}
          </div>
        ))}
      </div>
    </div>
  )
}
