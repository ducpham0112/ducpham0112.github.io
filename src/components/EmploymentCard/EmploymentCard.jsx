import styles from './EmploymentCard.module.css'

export default function EmploymentCard({ position, company, period, responsibilities, skills }) {
  return (
    <div className={styles.card}>
      <div className={styles.content}>
        <div className={styles.header}>
          <h3 className={styles.position}>{position}</h3>
          <span className={styles.period}>{period}</span>
        </div>
        <div className={styles.company}>{company}</div>
        {responsibilities.length > 0 && (
          <ul className={styles.responsibilities}>
            {responsibilities.map((r, i) => (
              <li key={i}>{r}</li>
            ))}
          </ul>
        )}
        {skills.length > 0 && (
          <div className={styles.skills}>
            {skills.map((s) => (
              <span key={s} className={styles.chip}>{s}</span>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
