import EmploymentCard from '../EmploymentCard/EmploymentCard'
import styles from './EmploymentTimeline.module.css'

export default function EmploymentTimeline({ employment }) {
  return (
    <section className={styles.section}>
      <h2 className={styles.title}>Employment History</h2>
      <div className={styles.timeline}>
        {employment.map((job, i) => (
          <EmploymentCard key={i} {...job} />
        ))}
      </div>
    </section>
  )
}
