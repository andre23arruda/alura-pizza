import { useEffect, useState } from 'react'
import Dish from 'components/Dish'
import { DishProps } from 'types/Dishes'
import styles from './App.module.scss'

const BASE_API_URL = process.env.REACT_APP_API_URL
const LOCAL = process.env.REACT_APP_LOCAL
const API_URL  = `http${ LOCAL ? '' : 's'}://${ BASE_API_URL }`

export default function App() {

    const [dishes, setDishes] = useState<DishProps[]>([])

    useEffect(() => {
        fetch(`${ API_URL }/api/dishes/`)
        .then(response => response.json())
        .then(data => setDishes(data))
    }, [])

    return (
        <div className={ styles.App }>
            <div className={ styles.bannerContainer }>
                <img
                    src="/assets/images/banner.png"
                    alt="Banner Cardápio"
                />
            </div>

            <div className={ styles.logoContainer }>
                <img
                    className={ styles.logo }
                    src="/assets/images/logo.svg"
                    alt="Logo Alura Pizza" />
            </div>

            <section className={ styles.menu }>
                { dishes.map(dish => (
                    <Dish
                        key={ dish.id }
                        {...dish}
                    />
                ))}
            </section>

            <footer>
                <p className={ styles.footerText }>
                    Feito com carinho por quem entende de pizza gostosa!!
                </p>
            </footer>
        </div>
    )
}
