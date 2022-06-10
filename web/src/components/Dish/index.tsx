import { DishProps } from 'types/Dishes'
import styles from './Dish.module.scss'

export default function Dish({ name, description, price, image }: DishProps) {
	return (
		<div className={ styles.Dish }>
			<div className={ styles.imageContainer }>
				<img src={ image } alt={ name } />
			</div>

			<div className={ styles.content }>
				<p>
					<strong>{ name }</strong>
				</p>

				<p>{ description }</p>

				<p>
					<strong>R$ { price }</strong>
				</p>
			</div>
		</div>
	)
}
